import json
import pytest
from collections import defaultdict
from dataclasses import asdict
from datetime import datetime, timedelta
from typing import List
from flask import Response
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy

from dtos import VisitorResponseV2
from dtos.v2.qa_model_dto_v2 import QAModelCreateRequestV2
from models import Visitor
from models import Data
from models import QAModel
from services import DataService
from services import QAModelService
from services.visitor_service import VisitorService
from tests.mock.dtos.v2 import MockQAModelCreateRequestV2


@pytest.mark.qa_model
def test_create_qa_model(app: FlaskClient, 
                         db: SQLAlchemy,
                         visitor_model: List[Visitor], 
                         visitor_service: VisitorService):

    url = '/v2/models'
    dto: QAModelCreateRequestV2 = MockQAModelCreateRequestV2()

    visitor_service.create(visitor_model)
    dto.visitor = VisitorResponseV2.from_model(visitor_model[0])
    dto = asdict(dto)

    response: Response = app.post(url,
                                  data=json.dumps(dto),
                                  content_type='application/json')

    assert response.status_code == 200

    response = response.get_json()

    assert response["ml_type"] == dto["ml_type"]
    assert response["ml_version"] == dto["ml_version"]
    assert response["bleu_score"] == dto["bleu_score"]
    assert response["rouge_score"] == dto["rouge_score"]
    assert response["meteor_score"] == dto["meteor_score"]

    model = QAModel.query.first()
    db.session.delete(model)
    db.session.commit()

@pytest.mark.qa_model
def test_read_qa_model(app: FlaskClient, 
                       qa_model_service: QAModelService, 
                       qa_model_model: QAModel):
    
    qa_model_service.create(qa_model_model)

    url = '/v2/models/' + str(qa_model_model.id)

    response: Response = app.get(url, content_type='application/json')

    assert response.status_code == 200
    response = response.get_json()
    assert response["id"] == qa_model_model.id


@pytest.mark.qa_model
def test_read_latest_qa_model_by_type(app: FlaskClient, 
                                      qa_model_service: QAModelService, 
                                      qa_model_model_list: List[QAModel]):

    url = 'v2/models/BERT/latest'

    latest_model = max(qa_model_model_list,
                       key=lambda q: q.created_date)

    for qa_model in qa_model_model_list:
        qa_model.ml_type = 'BERT'
        qa_model_service.create(qa_model)

    response: Response = app.get(url, content_type='application/json')

    assert response.status_code == 200

    response = response.get_json()
    assert response["ml_type"] == 'BERT'
    assert int(response["id"]) == latest_model.id


@pytest.mark.qa_model
def test_read_latest_models(app: FlaskClient, 
                            qa_model_service: QAModelService, 
                            qa_model_model_list: QAModel):

    url = '/v2/models/latest'

    for qa_model in qa_model_model_list:
        qa_model_service.create(qa_model)

    groups = defaultdict(list)
    for qa_model in qa_model_model_list:
        groups[qa_model.ml_type].append(qa_model)

    latest_models = []
    for group in groups.values():
        group.sort(key=lambda q: q.created_date, reverse=True)
        latest_models.append(group[0])

    response: Response = app.get(url, content_type='application/json')

    assert response.status_code == 200

    response: List[dict] = response.get_json()
    assert len(latest_models) == len(response)


@pytest.mark.qa_model
def test_read_best_models(app: FlaskClient, 
                          qa_model_service: QAModelService, 
                          qa_model_model_list: QAModel):

    url = '/v2/models/best'

    for qa_model in qa_model_model_list:
        qa_model_service.create(qa_model)

    response: Response = app.get(url, content_type='application/json')

    assert response.status_code == 200
    response: List[dict] = response.get_json()
    assert len(response) > 0


@pytest.mark.qa_model
def test_get_word_cloud(app: FlaskClient,
                        qa_model_service: QAModelService, 
                        qa_model_model: QAModel,
                        data_service: DataService, 
                        data_model_list: List[Data]):

    # Model needs to be in the future so it can find the mock data that will have a date of today
    qa_model_model.created_date = datetime.today() + timedelta(days=5)
    qa_model_service.create(qa_model_model)
    for data in data_model_list:
        data_service.create(data)

    url = f'/v2/models/{qa_model_model.id}/wordcloud'

    response: Response = app.get(url, content_type='application/json')

    word_cloud: dict = response.get_json()

    assert response.status_code == 200
    assert word_cloud["model_id"] == qa_model_model.id
    assert len(word_cloud["words"]) == 100
    assert all("name" in e for e in word_cloud["words"])
    assert all("weight" in e for e in word_cloud["words"])


@pytest.mark.qa_model
def test_get_models_by_type(app: FlaskClient, 
                            qa_model_service: QAModelService, 
                            qa_model_model_list: List[QAModel]):
                            
    url = '/v2/models/BERT'

    for model in qa_model_model_list:
        model.ml_type = 'BERT'
        qa_model_service.create(model)

    response: Response = app.get(url, content_type='application/json')

    models: dict = response.get_json()

    assert response.status_code == 200
    assert len(models) == len(qa_model_model_list)
    assert all(e["ml_type"] == 'BERT' for e in models)
