from http.client import ResponseNotReady
import pytest
import json
from typing import List
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy
from dataclasses import asdict
from flask import Response
from dtos.v2.data_dto_v2 import DataUpdateRequestV2
from models.data_model import Data
from services.data_service import DataService

from tests.mock.dtos.v2 import MockDataCreateRequestV2
from dtos import DataCreateRequestV2
from models import Visitor, visitor_model
from dtos import VisitorResponseV2
from services import VisitorService, visitor_service
from tests.mock.dtos.v2.mock_data_dtos_v2 import MockDataUpdateRequestV2

@pytest.mark.data
def test_create_data(app: FlaskClient, 
                     db: SQLAlchemy,
                     visitor_model: List[Visitor], 
                     visitor_service: VisitorService):

    url = '/v2/data'
    dto: DataCreateRequestV2 = MockDataCreateRequestV2()

    visitor_service.create(visitor_model)
    dto.visitor = VisitorResponseV2.from_model(visitor_model[0])
    dto = asdict(dto)


    response: Response = app.post(url,
                                  data=json.dumps(dto),
                                  content_type='application/json')

    assert response.status_code == 200

    response = response.get_json()

    assert dto["tweet"] == response["tweet"]
    assert dto["question"] == response["question"]

    model = Data.query.first()
    db.session.delete(model)
    db.session.commit()

@pytest.mark.data
def test_read_data(app: FlaskClient, 
                   data_service: DataService,
                   data_model: Data):

    data_service.create(data_model)
    url = f'/v2/data/{data_model.id}'

    response: Response = app.get(url, content_type='application/json')

    assert response.status_code == 200
    response = response.get_json()
    assert response["id"] == data_model.id

@pytest.mark.data
def test_update_data(app: FlaskClient,
                     data_service: DataService,
                     data_model: Data,
                     visitor_model: Visitor,
                     visitor_service: VisitorService):
    
    visitor_service.create(visitor_model)
    data_service.create(data_model)

    dto: DataUpdateRequestV2 = MockDataUpdateRequestV2()
    dto.id = data_model.id

    dto.visitor = VisitorResponseV2.from_model(visitor_model[0])
    dto = asdict(dto)

    url = f'/v2/data/{data_model.id}'
    response: Response = app.put(url,
                                 data=json.dumps(dto),
                                 content_type='application/json')

    assert response.status_code == 200

    response = response.get_json()

    assert response["id"] == dto["id"]
    assert response["qid"] == dto["qid"]
    assert response["answer"] == dto["answer"]
    assert response["start_position"] == dto["start_position"]
    assert response["end_position"] == dto["end_position"]

    