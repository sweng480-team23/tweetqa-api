import pytest
import json
from flask import Response
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy
from dataclasses import asdict
from typing import List
from dtos import PredictionCreateRequestV2
from dtos import VisitorResponseV2
from dtos.v2.prediction_dto_v2 import PredictionUpdateRequestV2
from models import Prediction
from models import Data
from models import Visitor
from services import VisitorService
from services.prediction_service import PredictionService
from tests.mock.dtos.v2.mock_prediction_dtos_v2 import MockPredictionCreateRequestV2, MockPredictionUpdateRequestV2 


pytest.mark.prediction
def test_create_prediction(app: FlaskClient, 
                           db: SQLAlchemy,
                           visitor_model: List[Visitor], 
                           visitor_service: VisitorService):

    url = '/v2/predictions'
    dto: PredictionCreateRequestV2 = MockPredictionCreateRequestV2()

    visitor_service.create(visitor_model)
    dto.visitor = VisitorResponseV2.from_model(visitor_model[0])
    dto = asdict(dto)

    response: Response = app.post(url,
                                  data=json.dumps(dto),
                                  content_type='application/json')

    assert response.status_code == 200

    response = response.get_json()

    visitor_dto = dto["visitor"]
    visitor_response = response["visitor"]

    assert visitor_dto["token"] == visitor_response["token"]
    assert visitor_dto["id"] == visitor_response["id"]

    data_dto = dto["datum"]
    data_response = response["datum"]

    assert data_dto["tweet"] == data_response["tweet"]
    assert data_dto["question"] == data_response["question"]

    prediction_model = Prediction.query.first()
    data_model = Data.query.first()
    db.session.delete(prediction_model)
    db.session.delete(data_model)
    db.session.commit()

def test_read_prediction(app: FlaskClient,
                         visitor_model: List[Visitor],
                         visitor_service: VisitorService,
                         prediction_model: Prediction,
                         prediction_service: PredictionService):

    visitor_service.create(visitor_model)
    prediction_model.visitor = visitor_model[0]
    prediction_service.create(prediction_model)
    url = f'/v2/predictions/{prediction_model.id}'

    response: Response = app.get(url, content_type='application/json')

    assert response.status_code == 200

    response = response.get_json()
    assert response["id"] == prediction_model.id 
    assert response["prediction"] == prediction_model.prediction

    data_response = response["datum"]
    data: Data = prediction_model.datum

    assert data_response["tweet"] == data.tweet
    assert data_response["question"] == data.question

def test_update_prediciton(app: FlaskClient,
                           visitor_model: List[Visitor],
                           visitor_service: VisitorService,
                           prediction_model: Prediction,
                           prediction_service: PredictionService):

    visitor_service.create(visitor_model)
    prediction_model.visitor = visitor_model[0]
    prediction_service.create(prediction_model)
    url = f'/v2/predictions/{prediction_model.id}'

    dto: PredictionUpdateRequestV2 = MockPredictionUpdateRequestV2()
    dto.id = prediction_model.id
    dto.visitor = VisitorResponseV2.from_model(visitor_model[0])

    dto = asdict(dto)

    response: Response = app.put(url, 
                                 data = json.dumps(dto),
                                 content_type='application/json')

    assert response.status_code == 200

    response = response.get_json()

    assert dto["id"] == response["id"]

    visitor_dto = dto["visitor"]
    visitor_response = response["visitor"]

    assert visitor_dto["token"] == visitor_response["token"]
    assert visitor_dto["id"] == visitor_response["id"]