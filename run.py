
from services.DataService import DataService
from models.DataModel import DataModel
from datetime import datetime

test_data =  DataModel(
    qid = '0c871b7e5320d0816d5b2979d67c2655',
    tweet = ('Test 1 - Our prayers are with the students, educators & families at '+
    'Independence High School & all the first responders on the scene. ' +
    '#PatriotPride\u2014 Doug Ducey (@dougducey) February 12, 2016'), 
    question = 'at which school were first responders on the scene for?',
    answer = 'independence high school',
    created = datetime.now(),
    updated = datetime.now(),
    original = True,
    start_position = 60,
    end_position = 84,    
)

DataService.create_data(test_data)