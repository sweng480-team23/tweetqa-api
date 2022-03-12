
from select import select
import pytest
from flask_sqlalchemy import SQLAlchemy
from typing import List
from datetime import datetime, timedelta

from services import DataService
from services import QAModelService
from models import Data
from models import QAModel
from tests.mock.dtos.v2 import MockDataCreateRequestV2
from tqatypes.word_response import WordResponse


@pytest.mark.data
def test_data_service_create(data_model: Data, data_service: DataService):

    data_out = data_service.create(data_model)
    data_saved = Data.query.filter(Data.id == data_model.id).first()

    assert data_saved is not None
    assert data_out is not None
    assert data_saved == data_out
    assert data_out == data_model


@pytest.mark.data
def test_data_service_read(data_model: Data, data_service: DataService):

    data_service.create(data_model)
    data_out = data_service.read_by_id(data_model.id)

    assert data_out is not None
    assert data_out == data_model


@pytest.mark.data
def test_data_service_update(data_model: Data, data_service: DataService):

    data_service.create(data_model)

    data_model.qid = 'updated qid'
    data_out = data_service.update(data_model)

    assert data_out is not None
    assert data_out == data_model


@pytest.mark.data
def test_read_all_data_since(data_model_list: List[Data], data_service: DataService):

    min_date = datetime.today() + timedelta(days=7)
    for data in data_model_list:
        data_service.create(data)

        # Find oldest entry
        if min_date > data.created_date:
            min_date = data.created_date

    min_date = min_date - timedelta(days=7)

    selected_data: List[Data] = data_service.read_all_data_since(min_date)

    assert type(selected_data) == list
    assert all(type(e) == Data for e in selected_data)
    assert len(selected_data) == len(data_model_list)
    assert all(e.created_date > min_date for e in selected_data)


@pytest.mark.data
def test_read_last_x_datum(data_model_list: List[Data], data_service: DataService):

    for data in data_model_list:
        data_service.create(data)

    n = len(data_model_list)
    selected_data: List[Data] = data_service.read_last_x_datum(n//2)

    assert type(selected_data) == list
    assert all(type(e) == Data for e in selected_data)
    assert len(selected_data) == n//2
    for i, j in zip(range(n-1, n//2-1, -1), range(n//2-1, -1, -1)):
        assert selected_data[j] == data_model_list[i]


@pytest.mark.data
def test_generate_word_cloud(data_model_list: List[Data], data_service: DataService,
                             qa_model_model: QAModel, qa_model_service: QAModelService):

    qa_model_model.created_date = datetime.today() - timedelta(days=5)
    qa_model_service.create(qa_model_model)
    for data in data_model_list:
        data_service.create(data)

    id = qa_model_model.id
    word_counts: List[WordResponse] = data_service.generate_word_cloud(id)

    assert type(word_counts) == list
    assert all(type(e) == dict for e in word_counts)
    assert len(word_counts) == 100
