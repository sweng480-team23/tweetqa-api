import re
from transformers import BertTokenizer, TFBertModel
import tensorflow as tf


class TFBertModelRunner(object):
    tokenizer: BertTokenizer
    model: TFBertModel

    def __init__(self, tokenizer: BertTokenizer, model: TFBertModel) -> None:
        self.tokenizer = tokenizer
        self.model = model
        super().__init__()

    def answer_tweet_question(self, tweet, question):
        input_dict = self.tokenizer(question, tweet, return_tensors="tf")
        outputs = self.model(input_dict)
        start_logits = outputs.start_logits
        end_logits = outputs.end_logits
        all_tokens = self.tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
        answer = " ".join(all_tokens[tf.math.argmax(start_logits, 1)[0]:tf.math.argmax(end_logits, 1)[0] + 1])
        answer_fixed = re.sub(r'\s##', '', answer)
        return answer_fixed
