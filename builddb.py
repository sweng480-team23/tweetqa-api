from controllers import db
from models.AccountModel import Account
from models import *
from datetime import datetime
import uuid
    
# Reset database
db.drop_all()
db.create_all()


testdata = Data(
    qid = '0c871b7e5320d0816d5b2979d67c2649',
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

testmodel = QAModel(
    ml_type = 'BERT',
    ml_version = '0.1.0',
    bleu_score = 0.70,
    rouge_score = 0.70,
    meteor_score = 0.70, 
    created_date = datetime.now()
)

testvisitor = Visitor(
    token_id = uuid.uuid1(),
    name = 'John',
    email = 'John@hotmail.com'
)

testprediction = Prediction(
    prediction = 'Kinder Garden',
    is_corrected = True,
    alt_answer = None,
    model_id = testmodel.id,
    model = testmodel, 
    datum_id = testdata.id,
    data = testdata,
    visitor_id = testvisitor.id,
    visitor = testvisitor
)

testaccount = Account(
    username = 'Johny',
    password = 'password',
    email = 'john.doe@gmail.com'
)

db.session.add(testdata)
db.session.add(testmodel)
db.session.add(testvisitor)
db.session.add(testprediction)
db.session.add(testaccount)
db.session.commit()

model = QAModel.query.order_by(QAModel.id.desc()).first()

print(model)
print(model.predictions[0])

db.session.close()