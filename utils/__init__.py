from utils.bert_model_runner import BertModelRunner, BertTokenizerFast, BertForQuestionAnswering



# print(' * Initializing model runners')

tokenizer = BertTokenizerFast.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
first_model = BertForQuestionAnswering.from_pretrained('utils/models/bert/v1')
first_runner = BertModelRunner('First BERT Model', tokenizer, first_model)

# print(' * Model runner init complete')

# print('############################# Testing model runner init #############################')
# tweet = "Our prayers are with the students, educators & families at Independence High School & all the first responders on the scene. #PatriotPride— Doug Ducey (@dougducey) February 12, 2016"
# question = "at which school were first responders on the scene for?"
# answer = first_runner.answer_tweet_question(tweet, question)
# print('Tweet: ' + tweet)
# print('Question: ' + question)
# print('Anwer: ' + answer[0])
# print('############################# Model runner testing complete #############################')
