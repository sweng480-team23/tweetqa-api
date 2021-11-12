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

def uuid_generator(size : int = 60) -> str:
    chars = string.ascii_lowercase + string.digits
    uuid = ''.join(random.choice(chars) for i in range(size))
    return uuid


test_data = Data(
    qid = '0c871b7e5320d0816d5b2979d67c2936',
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
#print(saved_data)
print(data_get)

#date_selected = datetime(2021, 11, 1)
#dataset = new_data_service.read_all_data_since(date_selected)
dataset = new_data_service.read_last_x_datum(2)
for data in dataset:
    print(data)

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