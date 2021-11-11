from controllers import db
from models.AccountModel import AccountModel
from models.DataModel import DataModel
from models.PredictionModel import PredictionModel
from models.QAModel import QAModel
from models.AccountModel import AccountModel
from datetime import datetime
import random, string


def uuid_generator(size : int = 60) -> str:
    chars = string.ascii_lowercase + string.digits
    uuid = ''.join(random.choice(chars) for i in range(size))
    return uuid

# Reset database
db.drop_all()
db.create_all()


dm1 = DataModel(
    qid = '0c871b7e5320d0816d5b2979d67c2649',
    tweet = ('Our prayers are with the students, educators & families at '+
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

m1 = QAModel(
    uuid = uuid_generator(),
    ml_type = 'BERT',
    ml_version = '0.1.0',
    bleu_score = 0.70,
    rogue_score = 0.70,
    meteor_score = 0.70, 
    created = datetime.now()
)

pm1 = PredictionModel(
    uuid = 1,
    token_id = uuid_generator(),
    is_corrected = False,
    alt_answer = None,
    model_id = m1.model_id,
    model = m1, 
    datum_id = dm1.datum_id,
    data = dm1
)

a1 = AccountModel(
    uuid = uuid_generator(),
    password = 'password',
    email = 'john.doe@gmail.com'
)

db.session.add(dm1)
db.session.add(m1)
db.session.add(pm1)
db.session.add(a1)

model = QAModel.query.order_by(QAModel.model_id.desc()).first()
print(model)
print(model.predictions[0])

db.session.commit()
db.session.close()