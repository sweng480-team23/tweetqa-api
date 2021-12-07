from flask.wrappers import Response
from controllers import app
from controllers import db
from flask_sqlalchemy import SQLAlchemy
from services.data_service import DataService
from datetime import datetime
from models import *
import json
import os

tester = app.app.test_client()

QA_MODEL_CONTROLLER_VERSION = 'v1'

def test_root():
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b'"The TweetQA Api is running!"\n'

def mock_db_setup():
    app.app.config['TESTING'] = True
    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.drop_all()
    db.create_all()
    db.session.commit()

def mock_db_teardown():
    db.session.close()
    os.remove('controllers/test.db')

def test_data_service_creates_data():
    mock_db_setup()

    data_in = Data(
        qid = 'test qid1',
        tweet = ('test tweet'),
        question = 'test question',
        answer = 'test answer',
        created_date = datetime.now(),
        updated_date = datetime.now(),
        source = "original dataset",
        start_position = 1,
        end_position = 4
    )

    data_service = DataService()
    data_out = data_service.create_data(data_in)
    actual_data = Data.query.filter(Data.id == data_in.id).first()
    mock_db_teardown()

    assert actual_data is not None
    assert data_out is not None
    assert actual_data == data_out
    assert data_out == data_in

def test_data_service_reads_data_by_id():
    mock_db_setup()

    data_in = Data(
        qid = 'test qid2',
        tweet = ('test tweet'),
        question = 'test question',
        answer = 'test answer',
        created_date = datetime.now(),
        updated_date = datetime.now(),
        source = "original dataset",
        start_position = 1,
        end_position = 4
    )

    db.session.add(data_in)
    db.session.commit()
    id = Data.query.first().id

    data_service = DataService()
    data_out = data_service.read_data_by_id(id)
    mock_db_teardown()

    assert data_out is not None
    assert data_out == data_in

def test_data_service_updates_data():
    mock_db_setup()

    data_in = Data(
        qid = 'test qid3',
        tweet = ('test tweet'),
        question = 'test question',
        answer = 'test answer',
        created_date = datetime.now(),
        updated_date = datetime.now(),
        source = "original dataset",
        start_position = 1,
        end_position = 4
    )

    db.session.add(data_in)
    db.session.commit()

    data_in.qid = 'updated qid'

    data_service = DataService()
    data_out = data_service.update_data(data_in)
    mock_db_teardown()

    assert data_out is not None
    assert data_out == data_in

def test_create_qa_model():
    '''TC-004: The create model end point is being reached and providing the appropriate response'''
    data = {}
    data["ml_type"] = "BERT-FINE-TUNED"
    data["ml_version"] = "1.1"
    data["bleu_score"] = 80.0
    data["rouge_score"] = 80.0
    data["meteor_score"] = 80.0
    mock_db_setup()

    response = tester.post('/'+ QA_MODEL_CONTROLLER_VERSION + '/models',
                            data=json.dumps(data),
                            content_type='application/json')

    mock_db_teardown()
    assert response.status_code == 200
    response = response.get_json()

    assert response["ml_type"] == data["ml_type"]
    assert response["ml_version"] == data["ml_version"]
    assert response["bleu_score"] == data["bleu_score"]
    assert response["rouge_score"] == data["rouge_score"]
    assert response["meteor_score"] == data["meteor_score"]

def test_read_qa_model():
    '''TC-005: The read model endpoint being reached and providing the appropriate response'''
    mock_db_setup()

    data_in = QAModel(
        ml_type = "BERT-FINE-TUNED",
        ml_version = "1.1",
        bleu_score = 80.0,
        rouge_score = 80.0,
        meteor_score = 80.0,
        created_date = datetime.now()
    )

    db.session.add(data_in)
    db.session.commit()

    response = tester.get('/' + QA_MODEL_CONTROLLER_VERSION + '/models/1',
                           content_type='application/json')

    mock_db_teardown()
    assert response.status_code == 200
    response = response.get_json()
    assert response["id"] == 1

def test_read_latest_qa_model_by_type():
    '''TC-006: The read latest model by type end point is being reached and providing the appropriate response'''
    mock_db_setup()

    data_in = QAModel(
        ml_type = "BERT",
        ml_version = "1.1",
        bleu_score = 80.0,
        rouge_score = 80.0,
        meteor_score = 80.0,
        created_date = datetime.now()
    )

    db.session.add(data_in)
    db.session.commit()
    response = tester.get('/' + QA_MODEL_CONTROLLER_VERSION + '/models/BERT',
                           content_type='application/json')

    mock_db_teardown()
    assert response.status_code == 200
    response = response.get_json()
    assert response["ml_type"] == 'BERT'

def test_read_latest_models():
    '''TC-007: The read latest models endpoint is being reached and providing the appropriate response'''
    mock_db_setup()
    response = tester.get('/' + QA_MODEL_CONTROLLER_VERSION + '/models/latest',
                           content_type='application/json')

    mock_db_teardown()
    assert response.status_code == 200
    response = response.get_json()

    assert response["length"] != 1
