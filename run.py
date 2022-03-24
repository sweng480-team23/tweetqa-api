from operator import ne

from numpy import save
from controllers import db


# from models.prediction_model import Prediction
# from models.qa_model import QAModel
# # from models.visitor_model import Visitor

from datetime import datetime
import random, string
from controllers.v2.account_controller_v2 import AccountsView
# from services.prediction_service import PredictionService
# from services.qa_model_service import QAModelService

""" Menu:
1. Manual test code for data service class
2. Manual test code for account service class
3. Manual test code for visitor service class 
4. Manual test code for prediction service class
5. Manual test code for model service class
6. Script to automatically import data from db - TODO: add this into the function for data_service. 
"""

""" # 1. Manual test code for data service class
from models.data_model import Data
from services.data_service import DataService
test_data = Data(
    qid = '0c871b7e5320d0816d5b2999d68c2936',
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
#saved_data = new_data_service.create(test_data)
#print(saved_data)
data_get = new_data_service.read_by_id(3)
print(data_get)
data_get.source = 'original set'
updated_data = new_data_service.update(data_get)
print(updated_data)
#print(data_get)

#date_selected = datetime(2021, 11, 1)
#dataset = new_data_service.read_all_data_since(date_selected)
#dataset = new_data_service.read_last_x_datum(2)
#for data in dataset:
#    print(data) """



#2. Manual test code for account service class
from models.account_model import Account
from services.account_service import AccountService
testaccount = Account(
    password = 'password',
    email = 'abc@gmail.com'
)

new_accservice = AccountService()
new_accservice.create(testaccount)
get_account = new_accservice.login('abc@gmail.com','password')
print(get_account)

new_accCon = AccountsView()

login_dict = {"email":"abc@gmail.com","password":"password"}
login_response = new_accCon.admin_login(login_dict)
print(login_response)
# print (new_accservice.generate_token_invitation_for_email('newbie@gmail.com'))

# #3. Manual test code for visitor service class
# from models.visitor_model import Visitor
# from services.visitor_service import VisitorService
# print (VisitorService().visitor_check('e80a9052-7983-45fc-9707-5c1e3915878a'))

""" #4. Manual test code for prediction service class
testprediction = Prediction(
    prediction = 'Good',
    is_correct = True,
    alt_answer = 'Model',
    model_id = 1,
    datum_id = 4,
    visitor_id = 1
)

new_predservice = PredictionService()
#saved_prediction = new_predservice.create(testprediction)

# testprediction.uuid = '0mpzsz22qebxk4qfkatm3tnyc5syryz4t5z7lik8cm1ct95ahyroyv3hsh3t'
testprediction.id = 4
testprediction.alt_answer = 'looking good'
testprediction.is_corrected = False
saved_prediction = new_predservice.update(testprediction)
print(saved_prediction) """

""" #5. Manual test code for model service class
new_modalservice = QAModelService()

testmodel = QAModel(
    #id = 2,
    created_date = datetime.now(),
    model_url = "testing456",
    ml_type = 'BERT_new2',
    ml_version = '0.1.12',
    bleu_score = 0.75,
    rouge_score = 0.75,
    meteor_score = 0.75
    )

#saved_model = new_modalservice.create(testmodel)
#saved_model = new_modalservice.read_latest_qa_model_by_type('BERT')
#print(saved_model)
#saved_models = new_modalservice.read_all_qa_model_by_type('BERT')
#print(saved_models)
saved_models2 = new_modalservice.read_latest_models()
print(saved_models2) """





""" # scripts to import json file with starting and ending position into database
#import dependencies
import pandas as pd
import string

#import data set
data = pd.read_json('https://raw.githubusercontent.com/sweng480-team23/tweet-qa-data/main/train.json')
# print(data.head(5))

# #required to transform the data, explore this later : CSJ
# data["Answer"] = data["Answer"].explode()

# #selecting first five
data_selected = data
#turning it into dictionary (list)
data_selected_preprocess = data_selected.to_dict('records')
#print(data_selected_preprocess)
# #tweet = data_selected_preprocess[2]["Tweet"].lower()
# #function returning a dictionary adding starting and ending position
# def identify_start_and_end_positions(data: dict) -> dict:
#   tweet = data["Tweet"].lower()
#   question = data["Question"].lower()
#   answer = data["Answer"].lower()
#   start_position = tweet.find(answer)

#   if start_position > -1:
#     end_position = start_position + len(answer)
#   else:
#     end_position = -1

#   return {
#       "qid": data["qid"],
#       "tweet": tweet,
#       "question": question,
#       "answer": answer,
#       "start_position": start_position,
#       "end_position": end_position,
#       # "bleu_score": max_score
#   }
# data_selected_processed = [identify_start_and_end_positions(datum) for datum in data_selected_preprocess[:]]

# print(len(data_selected_processed))
# no_pos_indentified = 0

# for datum in data_selected_processed:
#     if datum["start_position"] == -1 :
#         no_pos_indentified += 1

# print(no_pos_indentified)
#for datum in data_selected_processed:
#    print(datum)

# Function to save each data set from the dict into the sql instance

from models.data_model import Data
from services.data_service import DataService

def transform_and_save(data:dict):
    new_dataservice = DataService()
    for datum in data:
        test_data = Data(
            qid = datum["qid"],
            tweet = datum["Tweet"],
            question = datum["Question"],
            answer = datum["Answer"],
            created_date = datetime.now(),
            updated_date = datetime.now(),
            source = "original dataset",
            start_position = "0",
            end_position = "0"
        )
        try:
            saved_data = new_dataservice.create(test_data)
            #print(saved_data)
            #print("data saved")
        except Exception as e:
            #print(e)
            pass
# End of transform_and_save

transform_and_save(data_selected_preprocess) """

