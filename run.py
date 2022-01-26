from operator import ne
from controllers import db
# from models.account_model import Account
# from models.data_model import Data
# from models.prediction_model import Prediction
from models.qa_model import QAModel
# from models.visitor_model import Visitor
# from services.account_service import AccountService
from datetime import datetime
import random, string

# from services.data_service import DataService
# from services.prediction_service import PredictionService
from services.qa_model_service import QAModelService

# def uuid_generator(size : int = 60) -> str:
#     chars = string.ascii_lowercase + string.digits
#     uuid = ''.join(random.choice(chars) for i in range(size))
#     return uuid

"""
test_data = Data(
    qid = '0c871b7e5320d0816d5b2999d67c2936',
    uuid = uuid_generator(),
    tweet = ('Our prayers are with the students, educators & families at '+
    'Independence High School & all the first responders on the scene. ' +
    '#PatriotPride\u2014 Doug Ducey (@dougducey) February 12, 2016'),
    question = 'at which school were first responders on the scene for?',
    answer = 'independence high school',
    created_date = datetime.now(),
    updated_date = datetime.now(),
    source = "original dataset",
    start_position = 60,
    end_position = 84
)

new_data_service = DataService()
#saved_data = new_data_service.create_data(test_data)
data_get = new_data_service.read_data_by_qid(test_data.qid)
data_get.source = 'original set'
saved_data = new_data_service.update_data(data_get)
print(saved_data)
#print(data_get)

#date_selected = datetime(2021, 11, 1)
#dataset = new_data_service.read_all_data_since(date_selected)
#dataset = new_data_service.read_last_x_datum(2)
#for data in dataset:
#    print(data)
"""
"""

testaccount = Account(
    uuid = uuid_generator(),
    username = 'Johny',
    password = 'password',
    email = 'john.doe@gmail.com'
)

new_accservice = AccountService()
new_accservice.create_account(testaccount)
get_account = new_accservice.read_account('Johny2')
#get_account = new_accservice.login('Johny2','password')
print(get_account)
"""
"""
testprediction = Prediction(
    uuid = uuid_generator(),
    prediction = 'Good',
    is_corrected = True,
    alt_answer = 'Good',
    model_id = 1,
    datum_id = 1,
    visitor_id = 1
)

new_predservice = prediction_service()
#saved_prediction = new_predservice.create_prediction(testprediction)

testprediction.uuid = '0mpzsz22qebxk4qfkatm3tnyc5syryz4t5z7lik8cm1ct95ahyroyv3hsh3t'
testprediction.alt_answer = 'looking good'
testprediction.is_corrected = False
saved_prediction = new_predservice.update_prediction(testprediction)
print(saved_prediction)
"""
new_modalservice = QAModelService()

testmodel = QAModel(
    created_date = datetime.now(),

    ml_type = 'BERT',
    ml_version = '0.1.1',

    bucket = 'testing_bucket',
    location = 'testing_location',
    name = 'testing_name',

    training_started = datetime.now(),
    training_ended = datetime.now(),
    epochs = 12,
    batch_size_train = 12,
    batch_size_eval = 2,
    learning_rate = 0.0005,

    bleu_score = 0.70,
    rouge_score = 0.70,
    meteor_score = 0.70
    )

saved_model = new_modalservice.create_qa_model(testmodel)
#saved_model = new_modalservice.read_qa_model_by_uuid('wekcjl1f8bq0s3vypu221shqz2egx62pzjnmounduzwcgj71v10q6eb833vp')
#saved_model = new_modalservice.read_latest_qa_model_by_type('BERT')
print(saved_model)
# saved_models = new_modalservice.read_all_qa_model_by_type('BERT')

# for model in saved_models:
#     print(model) """



# scripts to import json file with starting and ending position into database
#import dependencies
import pandas as pd
import string

#import data set
data = pd.read_json('https://raw.githubusercontent.com/sweng480-team23/tweet-qa-data/main/train.json')
print(data.head(5))

#required to transform the data, explore this later : CSJ
data["Answer"] = data["Answer"].explode()

#selecting first five
data_selected = data
#turning it into dictionary (list)
data_selected_preprocess = data_selected.to_dict('records')
#tweet = data_selected_preprocess[2]["Tweet"].lower()
#function returning a dictionary adding starting and ending position
def identify_start_and_end_positions(data: dict) -> dict:
  tweet = data["Tweet"].lower()
  question = data["Question"].lower()
  answer = data["Answer"].lower()
  start_position = tweet.find(answer)

  if start_position > -1:
    end_position = start_position + len(answer)
  else:
    end_position = -1

  return {
      "qid": data["qid"],
      "tweet": tweet,
      "question": question,
      "answer": answer,
      "start_position": start_position,
      "end_position": end_position,
      # "bleu_score": max_score
  }
data_selected_processed = [identify_start_and_end_positions(datum) for datum in data_selected_preprocess[:]]

print(len(data_selected_processed))
no_pos_indentified = 0

for datum in data_selected_processed:
    if datum["start_position"] == -1 :
        no_pos_indentified += 1

print(no_pos_indentified)
#for datum in data_selected_processed:
#    print(datum)

# Function to save each data set from the dict into the sql instance
def transform_and_save(data:dict):
    new_dataservice = DataService()
    for datum in data:
        test_data = Data(
            qid = datum["qid"],
            tweet = datum["tweet"],
            question = datum["question"],
            answer = datum["answer"],
            created_date = datetime.now(),
            updated_date = datetime.now(),
            source = "original dataset",
            start_position = datum["start_position"],
            end_position = datum["end_position"],
        )
        saved_data = new_dataservice.create_data(test_data)
        print(saved_data)
# End of transform_and_save

#transform_and_save(data_selected_processed)

