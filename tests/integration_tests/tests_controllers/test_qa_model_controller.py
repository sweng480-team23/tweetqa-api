import pytest
import json
from datetime import datetime
from flask import Response
from flask_sqlalchemy import SQLAlchemy
from flask.testing import FlaskClient

from models import QAModel

CONTR_VER = 'v1'

@pytest.fixture
def qa_model_model():
    qa_model = QAModel(
        ml_type="BERT-FINE-TUNED",
        ml_version="1.1",
        bleu_score=80.0,
        rouge_score=80.0,
        meteor_score=80.0,
        created_date=datetime.now()
    )

    yield qa_model

@pytest.mark.qa_model
def test_create_qa_model(app: FlaskClient):
    """
    TC-004: The create model end point is being reached and providing the appropriate response
    """

    data = {}
    data["ml_type"] = "BERT-FINE-TUNED-V2"
    data["ml_version"] = "1.1"
    data["bleu_score"] = 80.0
    data["rouge_score"] = 80.0
    data["meteor_score"] = 80.0

    response: Response = app.post(f'/{CONTR_VER}/models',
                           data=json.dumps(data),
                           content_type='application/json')

    assert response.status_code == 200
    response = response.get_json()

    assert response["ml_type"] == data["ml_type"]
    assert response["ml_version"] == data["ml_version"]
    assert response["bleu_score"] == data["bleu_score"]
    assert response["rouge_score"] == data["rouge_score"]
    assert response["meteor_score"] == data["meteor_score"]

@pytest.mark.qa_model
def test_read_qa_model(db: SQLAlchemy, app: FlaskClient, qa_model_model: QAModel):
    """
    TC-005: The read model endpoint being reached and providing the appropriate response
    """

    db.session.add(qa_model_model)
    db.session.commit()

    response: Response = app.get(f'/{CONTR_VER}/models/1',
                          content_type='application/json')

    assert response.status_code == 200
    response = response.get_json()
    assert response["id"] == 1

@pytest.mark.qa_model
def test_read_latest_qa_model_by_type(db: SQLAlchemy, app: FlaskClient, qa_model_model: QAModel):
    """
    TC-006: The read latest model by type end point is being reached and providing the appropriate response
    """
    
    qa_model_model.ml_type = 'BERT'

    db.session.add(qa_model_model)
    db.session.commit()
    response: Response = app.get(f'/{CONTR_VER}/models/BERT/latest',
                          content_type='application/json')

    assert response.status_code == 200
    response = response.get_json()
    assert response["ml_type"] == 'BERT'

@pytest.mark.qa_model
def test_read_latest_models(db: SQLAlchemy, app: FlaskClient, qa_model_model: QAModel):
    """
    TC-007: The read latest models endpoint is being reached and providing the appropriate response
    """
    response: Response = app.get(f'/{CONTR_VER}/models/latest',
                          content_type='application/json')

    assert response.status_code == 200
    response = response.get_json()

    assert response["length"] != 1

@pytest.mark.qa_model
def test_get_word_cloud(app: FlaskClient):
    response: Response = app.get(f'/{CONTR_VER}/models/1/wordcloud', 
                                 content_type='application/json')

    word_cloud: dict = json.loads(response.get_data())

    assert response.status_code == 200
    assert word_cloud['model_id'] == 1
    assert len(word_cloud['words']) > 0
    assert 'name' in word_cloud['words'][0]

@pytest.mark.qa_model
def test_read_all_qa_model_by_type(app: FlaskClient):
    response: Response = app.get(f'/{CONTR_VER}/models/BERT', 
                                    content_type='application/json')
    models: dict = json.loads(response.get_data())
    assert response.status_code == 200
    assert len(models) > 0
    assert models[0]['ml_type'] == 'BERT'

