from operator import ne
from controllers import db
from models.AccountModel import Account
from models.DataModel import Data
from models.PredictionModel import Prediction
from models.QAModel import QAModel
from models.VisitorModel import Visitor
from services.AccountService import AccountService
from datetime import datetime
import random, string

from services.DataService import DataService
from services.PredictionService import PredictionService
from services.QAModelService import QAModelService

def uuid_generator(size : int = 60) -> str:
    chars = string.ascii_lowercase + string.digits
    uuid = ''.join(random.choice(chars) for i in range(size))
    return uuid

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

new_predservice = PredictionService()
#saved_prediction = new_predservice.create_prediction(testprediction)

testprediction.uuid = '0mpzsz22qebxk4qfkatm3tnyc5syryz4t5z7lik8cm1ct95ahyroyv3hsh3t'
testprediction.alt_answer = 'looking good'
testprediction.is_corrected = False
saved_prediction = new_predservice.update_prediction(testprediction)
print(saved_prediction)
"""
new_modalservice = QAModelService()

testmodel = QAModel(
    uuid = uuid_generator(),
    ml_type = 'BERT',
    ml_version = '0.1.0',
    bleu_score = 0.70,
    rogue_score = 0.70,
    meteor_score = 0.70, 
    created_date = datetime.now()
)

#saved_model = new_modalservice.create_qa_model(testmodel)
#saved_model = new_modalservice.read_qa_model_by_uuid('wekcjl1f8bq0s3vypu221shqz2egx62pzjnmounduzwcgj71v10q6eb833vp')
#saved_model = new_modalservice.read_latest_qa_model_by_type('BERT')
#print(saved_model)
saved_models = new_modalservice.read_all_qa_model_by_type('BERT')

for model in saved_models:
    print(model)
