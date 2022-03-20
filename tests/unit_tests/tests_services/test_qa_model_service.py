from collections import defaultdict
import pytest
from typing import List

from models import QAModel
from services import QAModelService


@pytest.mark.qa_model
def test_qa_model_service_create(qa_model_model: QAModel, qa_model_service: QAModelService):
    qa_model_out = qa_model_service.create(qa_model_model)
    qa_model_saved = QAModel.query.filter(
        QAModel.id == qa_model_model.id).first()

    assert qa_model_saved is not None
    assert qa_model_out is not None
    assert qa_model_saved == qa_model_out
    assert qa_model_out == qa_model_model


@pytest.mark.qa_model
def test_qa_model_service_read(qa_model_model: QAModel, qa_model_service: QAModelService):

    qa_model_service.create(qa_model_model)
    qa_model_out = qa_model_service.read_by_id(qa_model_model.id)

    assert qa_model_out is not None
    assert qa_model_out == qa_model_model


@pytest.mark.qa_model
def test_qa_model_service_update(qa_model_model: QAModel, qa_model_service: QAModelService):

    qa_model_service.create(qa_model_model)
    qa_model_model.ml_type = 'BERT-UPDATED'

    qa_model_out = qa_model_service.update(qa_model_model)

    assert qa_model_out is not None
    assert qa_model_out == qa_model_model


@pytest.mark.qa_model
def test_read_all_qa_model_by_type(qa_model_model_list: List[QAModel], qa_model_service: QAModelService):

    for qa_model in qa_model_model_list:
        qa_model.ml_type = 'BERT'
        qa_model_service.create(qa_model)

    selected_models: List[QAModel] = qa_model_service.read_all_qa_model_by_type(
        'BERT')

    assert type(selected_models) == list
    assert all(type(e) == QAModel for e in selected_models)
    assert len(selected_models) == len(qa_model_model_list)
    for i in range(len(qa_model_model_list)):
        assert qa_model_model_list[i] == selected_models[i]


@pytest.mark.qa_model
def test_read_latest_qa_model_by_type(qa_model_model_list: List[QAModel], qa_model_service: QAModelService):
    latest_model = max(qa_model_model_list,
                       key=lambda q: q.created_date)

    for qa_model in qa_model_model_list:
        qa_model.ml_type = 'BERT'
        qa_model_service.create(qa_model)

    selected_model = qa_model_service.read_latest_qa_model_by_type('BERT')
    assert selected_model is not None
    assert selected_model == latest_model


@pytest.mark.qa_model
def test_read_latest_models(qa_model_model_list: List[QAModel], qa_model_service: QAModelService):
    for qa_model in qa_model_model_list:
        qa_model_service.create(qa_model)

    groups = defaultdict(list)
    for qa_model in qa_model_model_list:
        groups[qa_model.ml_type].append(qa_model)

    latest_models = []
    for group in groups.values():
        group.sort(key=lambda q: q.created_date, reverse=True)
        latest_models.append(group[0])

    selected_models = qa_model_service.read_latest_models()

    assert type(selected_models) == list
    assert all(type(e) == QAModel for e in selected_models)
    assert all(not latest_models.remove(e) for e in selected_models)
    assert len(latest_models) == 0


@pytest.mark.qa_model
def test_read_best_model_by_type(qa_model_model_list: List[QAModel], qa_model_service: QAModelService):
    for qa_model in qa_model_model_list:
        qa_model_service.create(qa_model)

    selected_models = qa_model_service.read_best_model_by_type()

    assert type(selected_models) == list
    for selected_model in selected_models:
        assert QAModelService.average_model_scores(selected_model) >= max(
            [QAModelService.average_model_scores(qa_model)
             for qa_model in qa_model_model_list if qa_model.ml_type == selected_model.ml_type])
