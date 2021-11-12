from controllers import db
from models.AccountModel import Account
from models.DataModel import Data
from models.PredictionModel import Prediction
from models.QAModel import QAModel
from models.VisitorModel import Visitor
from datetime import datetime
import random, string


def uuid_generator(size : int = 60) -> str:
    chars = string.ascii_lowercase + string.digits
    uuid = ''.join(random.choice(chars) for i in range(size))
    return uuid

# Reset database
db.drop_all()
db.create_all()


testdata = Data(
    qid = '0c871b7e5320d0816d5b2979d67c2649',
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

testmodel = QAModel(
    uuid = uuid_generator(),
    ml_type = 'BERT',
    ml_version = '0.1.0',
    bleu_score = 0.70,
    rogue_score = 0.70,
    meteor_score = 0.70, 
    created_date = datetime.now()
)

testvisitor = Visitor(
    uuid = uuid_generator(),
    token_id = uuid_generator(),
    name = 'John',
    email = 'John@hotmail.com'
)
testprediction = Prediction(
    uuid = uuid_generator(),
    prediction = 'Kinder Garden',
    is_corrected = True,
    alt_answer = None,
    model_id = testmodel.model_id,
    model = testmodel, 
    datum_id = testdata.datum_id,
    data = testdata,
    visitor_id = testvisitor.visitor_id,
    visitor = testvisitor
)

testaccount = Account(
    uuid = uuid_generator(),
    username = 'Johny',
    password = 'password',
    email = 'john.doe@gmail.com'
)

db.session.add(testdata)
db.session.add(testmodel)
db.session.add(testvisitor)
db.session.add(testprediction)
db.session.add(testaccount)

model = QAModel.query.order_by(QAModel.model_id.desc()).first()
print(model)
print(model.predictions[0])

db.session.commit()
db.session.close()