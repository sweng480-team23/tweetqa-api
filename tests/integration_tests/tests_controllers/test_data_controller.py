# import pytest
# import json
# from typing import List
# from flask.testing import FlaskClient
# from flask_sqlalchemy import SQLAlchemy
# from dataclasses import asdict
# from flask import Response
# from models.data_model import Data

# from tests.mock.dtos.v2 import MockDataCreateRequestV2
# from dtos import DataCreateRequestV2
# from models import Visitor
# from dtos import VisitorResponseV2
# from services import VisitorService

# @pytest.mark.data
# def test_create_data(app: FlaskClient, visitor_model: List[Visitor], visitor_service: VisitorService):
#     url = '/v2/data'
#     dto: DataCreateRequestV2 = MockDataCreateRequestV2()

#     visitor_service.create(visitor_model)

#     model: Visitor = Visitor.query.first()
#     dto.visitor = VisitorResponseV2.from_model(model)
#     dto = asdict(dto)

#     print(Visitor.query.all())
#     response: Response = app.post(url,
#                                   data=json.dumps(dto),
#                                   content_type='application/json')
#     print(Visitor.query.all())

#     assert response.status_code == 200

#     response = response.get_json()

#     assert dto["tweet"] == response["tweet"]
#     assert dto["question"] == response["question"]


# @pytest.mark.data
# def test_read_Data(app: FlaskClient, db: SQLAlchemy, data_model: Data):
#     db.session.add(data_model)
#     db.session.commit()
    
#     url = '/v2/data/' + str(data_model.qid)

#     response: Response = app.get(url, content_type='application/json')

#     assert response.status_code == 200
#     response = response.get_json()
#     assert response["id"] == data_model.id