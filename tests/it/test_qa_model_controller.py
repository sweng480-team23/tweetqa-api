from controllers import app
import pytest
from flask import Response
import json


app.testing = True
client = app.app.test_client()


@pytest.mark.qa_model
def test_get_word_cloud():
    response: Response = client.get('/v1/models/1/wordcloud', content_type='application/json')
    word_cloud: dict = json.loads(response.get_data())
    assert response.status_code == 200
    assert word_cloud['model_id'] == 1
    assert len(word_cloud['words']) > 0
    assert 'name' in word_cloud['words'][0]


@pytest.mark.qa_model
def test_read_all_qa_model_by_type():
    response: Response = client.get('/v1/models/BERT', content_type='application/json')
    models: dict = json.loads(response.get_data())
    assert response.status_code == 200
    assert len(models) > 0
    assert models[0]['ml_type'] == 'BERT'
