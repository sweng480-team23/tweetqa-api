from dataclasses import asdict
import pytest
import json
from flask import Response
from flask_sqlalchemy import SQLAlchemy
from flask.testing import FlaskClient
from decouple import config

from models import QAModel
from tests.mock.dtos.v2 import MockQAModelCreateRequestV2

# @pytest.mark.qa_model
# def test_create_qa_model(app: FlaskClient, db: SQLAlchemy):
#     """
#     TC-004: The create model end point is being reached and providing the appropriate response
#     """
#     url = '/v2/models'
#     dto = MockQAModelCreateRequestV2()

#     response: Response = app.post(url,
#                            data=json.dumps(dto),
#                            content_type='application/json')

#     assert response.status_code == 200
#     response = response.get_json()

#     assert dto == response
    
    # assert response["ml_type"] == dto["ml_type"]
    # assert response["ml_version"] == dto["ml_version"]
    # assert response["bleu_score"] == dto["bleu_score"]
    # assert response["rouge_score"] == dto["rouge_score"]
    # assert response["meteor_score"] == dto["meteor_score"]

# @pytest.mark.qa_model
# def test_read_qa_model(db: SQLAlchemy, app: FlaskClient, qa_model_model: QAModel):
#     """
#     TC-005: The read model endpoint being reached and providing the appropriate response
#     """

#     db.session.add(qa_model_model)
#     db.session.commit()

#     response: Response = app.get(f'/v2/models/1',
#                           content_type='application/json')

#     assert response.status_code == 200
#     response = response.get_json()
#     assert response["id"] == 1

# @pytest.mark.qa_model
# def test_read_latest_qa_model_by_type(db: SQLAlchemy, app: FlaskClient, qa_model_model: QAModel):
#     """
#     TC-006: The read latest model by type end point is being reached and providing the appropriate response
#     """
    
#     qa_model_model.ml_type = 'BERT'

#     db.session.add(qa_model_model)
#     db.session.commit()
#     response: Response = app.get(f'/v2/models/BERT/latest',
#                           content_type='application/json')

#     assert response.status_code == 200
#     response = response.get_json()
#     assert response["ml_type"] == 'BERT'

# @pytest.mark.qa_model
# def test_read_latest_models(app: FlaskClient, qa_model_model: QAModel):
#     """
#     TC-007: The read latest models endpoint is being reached and providing the appropriate response
#     """
#     response: Response = app.get(f'/{V}/models/latest',
#                           content_type='application/json')

#     assert response.status_code == 200
#     response = response.get_json()

#     assert response["length"] != 1

# # TODO: Getting 404 response for this endpoint
# # @pytest.mark.qa_model
# # def test_get_word_cloud(db: SQLAlchemy, qa_model_model:QAModel, app: FlaskClient):

# #     model = db.session.query(QAModel).first()
# #     print(model)
# #     response: Response = app.get(f'/v2/models/{model.id}/wordcloud', 
# #                                  content_type='application/json')
# #     print(response)
# #     word_cloud: dict = json.loads(response.get_data())

# #     assert response.status_code == 200
# #     assert word_cloud['model_id'] == 1
# #     assert len(word_cloud['words']) > 0
# #     assert 'name' in word_cloud['words'][0]

# @pytest.mark.qa_model
# def test_read_all_qa_model_by_type(app: FlaskClient):

#     url = '/v2/models/BERT'

#     response: Response = app.get(url, 
#                                  content_type='application/json')
#     models: dict = json.loads(response.get_data())
#     assert response.status_code == 200
#     assert len(models) > 0
#     assert models[0]['ml_type'] == 'BERT'

