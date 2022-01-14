import pandas as pd
import numpy as np
import string
import json
import re

from typing import List
from os.path import exists
from google.cloud import storage
from nltk.translate.bleu_score import sentence_bleu
from nlgeval.pycocoevalcap.meteor.meteor import Meteor
from nlgeval.pycocoevalcap.rouge.rouge import Rouge
from transformers import BertTokenizerFast, BertForQuestionAnswering
from utils.bert_model_runner import BertModelRunner


local_model_location = './models'
gs_model_location = 'v2/artifacts/pipeline/TweetQA ML Pipeline/2c77f481-3c1d-404a-9421-54fee4d02a61/model-training/model'
config_file = 'config.json'
model_file = 'pytorch_model.bin'
training_args_file = 'training_args.bin'

meteor_scorer = Meteor()
rouge_scorer = Rouge()


def read_data(url: str) -> pd.DataFrame:
    return pd.read_json(url)


def download_model_to_local(gs_model_loc: str, model_name: str, model_loc: str):
    if (
        not exists(f'{model_loc}/{model_name}/{config_file}')
        and not exists(f'{model_loc}/{model_name}/{model_file}')
        and not exists(f'{model_loc}/{model_name}/{training_args_file}')
    ):
        bucket_name = 'tweetqa-models'
        storage_client = storage.Client.from_service_account_json('../gcp-keys/tweetqa-6233800255dc.json')
        bucket = storage_client.bucket(bucket_name)
        config_blob = bucket.blob(f'{gs_model_loc}/{config_file}')
        config_blob.download_to_filename(f'{model_loc}/{model_name}/{config_file}')
        model_blob = bucket.blob(f'{gs_model_loc}/{model_file}')
        model_blob.download_to_filename(f'{model_loc}/{model_name}/{model_file}')
        training_args_blob = bucket.blob(f'{gs_model_loc}/{training_args_file}')
        training_args_blob.download_to_filename(f'{model_loc}/{model_name}/{training_args_file}')


def get_model_runner(gs_model_loc: str, model_name: str, model_loc: str) -> BertModelRunner:
    download_model_to_local(gs_model_loc, model_name, model_loc)
    tokenizer = BertTokenizerFast.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    model = BertForQuestionAnswering.from_pretrained(f'{model_loc}/{model_name}')
    return BertModelRunner(model_name, tokenizer, model)


def generate_gold_file(df: pd.DataFrame) -> List[dict]:
    data_dict: dict = df.to_dict('records')
    return [{'qid': datum['qid'], 'Answer': datum['Answer']} for datum in data_dict]


def to_prediction(datum: dict, model_runner: BertModelRunner) -> dict:
    answer, start, end = model_runner.answer_tweet_question(datum['Tweet'], datum['Question'])
    print(start)
    return {
                'qid': datum['qid'],
                'Tweet': datum['Tweet'],
                'Question': datum['Question'],
                'Answer': answer,
                'Start': start,
                'End': end,
                'Actual Answer': datum['Answer']
            }


def generate_user_file(df: pd.DataFrame) -> List[dict]:
    model_runner: BertModelRunner = get_model_runner(gs_model_location, "bert", local_model_location)
    data_dict: dict = df.to_dict('records')
    return [to_prediction(datum, model_runner) for datum in data_dict]


def normalize_answer(s):
    """Lower text and remove punctuation, articles and extra whitespace."""

    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))


def ans_score(ans, gold_list):
    ans = normalize_answer(ans)
    gold_list = [normalize_answer(ref) for ref in gold_list]
    bleu = sentence_bleu([_.split() for _ in gold_list], ans.split(), weights=(1, 0, 0, 0))
    meteor, _ = meteor_scorer.compute_score({0: gold_list}, {0: [ans]})
    rouge, _ = rouge_scorer.compute_score({0: gold_list}, {0: [ans]})
    return {'bleu': bleu, 'meteor': meteor, 'rouge': rouge}


def evaluate(gold, pred):
    idx2gold = {item['qid']: item['Answer'] for item in gold}
    idx2pred = {item['qid']: item['Answer'] for item in pred}
    idx2scores = {}
    for id_ in idx2gold.keys():
        if isinstance(idx2pred[id_], list):
            pred_ans = idx2pred[id_][0]
        else:
            pred_ans = idx2pred[id_]
        idx2scores[id_] = ans_score(pred_ans, idx2gold[id_])
    bleus = [item['bleu'] for item in idx2scores.values()]
    meteors = [item['meteor'] for item in idx2scores.values()]
    rouges = [item['rouge'] for item in idx2scores.values()]
    print({'BLEU': np.mean(bleus), 'METEOR': np.mean(meteors), 'ROUGE': np.mean(rouges)})

    output = {}
    output['result'] = [
        {'test_split':
            {
                'BLEU-1': np.mean(bleus),
                'METEOR': np.mean(meteors),
                'ROUGE': np.mean(rouges)
            }
        }
    ]

    return output


if __name__ == '__main__':
    data: pd.DataFrame = read_data('https://raw.githubusercontent.com/sweng480-team23/tweet-qa-data/main/dev.json')
    gold_file = generate_gold_file(data)
    user_file = generate_user_file(data)

    with open('user_file.json', 'w') as f_out:
        json.dump(user_file, f_out)

    output = evaluate(gold_file, user_file)
    print(output)
