import connexion
from decouple import config

from flask_sqlalchemy import SQLAlchemy

app = connexion.App(__name__, specification_dir='./')
SECRET_KEY = config('SECRET_KEY')

# App Config
app.app.config['SECRET_KEY'] = SECRET_KEY


app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false'
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:' + SECRET_KEY + '@ljdub.com:3306/mysql_database'
db = SQLAlchemy(app.app)

app.add_api('../swagger.yml', pythonic_params=True)


# Model runner init
# TODO: legitimize the design for a model runner service, or similar pattern
# for demo purposes this works

from utils.bert_model_runner import BertModelRunner
from transformers import BertTokenizerFast, BertForQuestionAnswering

print(' * Initializing model runners')

tokenizer = BertTokenizerFast.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
first_model = BertForQuestionAnswering.from_pretrained('utils/models/bert/first')
first_runner = BertModelRunner('First BERT Model', tokenizer, first_model)

print(' * Model runner init complete')

print('############################# Testing model runner init #############################')
tweet = "Our prayers are with the students, educators & families at Independence High School & all the first responders on the scene. #PatriotPride— Doug Ducey (@dougducey) February 12, 2016"
question = "at which school were first responders on the scene for?"
answer = first_runner.answer_tweet_question(tweet, question)
print('Tweet: ' + tweet)
print('Question: ' + question)
print('Anwer: ' + answer)
print('############################# Model runner testing complete #############################')
