from dataclasses import asdict
import pytest
import json
from flask.testing import FlaskClient
from flask import Response
from flask_sqlalchemy import SQLAlchemy
from typing import List
from dtos.v2.visitor_dto_v2 import VisitorCreateRequestV2
from models import Visitor
from services.visitor_service import VisitorService
from tests.mock.dtos.v2.mock_visitor_dto_v2 import MockVisitorCreateRequestV2



@pytest.mark.visitor
def test_read_visitor(app: FlaskClient,
                      visitor_model: List[Visitor],
                      visitor_service: VisitorService):

    visitor_service.create(visitor_model)
    visitor = visitor_model[0]

    url = f'/v2/visitors/{visitor.id}'

    response: Response = app.get(url, content_type='application/json')

    assert response.status_code == 200
    response = response.get_json()

    assert response["id"] == visitor.id
    assert response["token"] == visitor.token
    

@pytest.mark.visitor
def test_get_by_token(app: FlaskClient,
                      visitor_model: List[Visitor],
                      visitor_service: VisitorService):

    visitor_service.create(visitor_model)
    visitor = visitor_model[0]

    url = f'/v2/visitors/{visitor.token}'

    response: Response = app.get(url, content_type='application/json')
    assert response.status_code == 200
    response = response.get_json()

    assert response["id"] == visitor.id
    assert response["token"] == visitor.token


@pytest.mark.visitor
def test_create_visitor(app: FlaskClient,
                        db: SQLAlchemy):

    url = 'v2/visitors'
    dto: VisitorCreateRequestV2 = MockVisitorCreateRequestV2()
    dto = asdict(dto)

    response: Response = app.post(url,
                                  data=json.dumps(dto),
                                  content_type='application/json')

    assert response.status_code == 200

    response = response.get_json()
    data = response["data"]
    assert all("token" in r for r in data)
    assert all("id" in r for r in data)

    models = Visitor.query.all()
    for model in models:
        db.session.delete(model)
        db.session.commit()