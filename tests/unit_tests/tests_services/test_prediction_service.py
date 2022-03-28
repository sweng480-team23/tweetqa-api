import pytest

from models.prediction_model import Prediction
from services.prediction_service import PredictionService


@pytest.mark.prediction
def test_prediction_service_create(prediction_model: Prediction, prediction_service: PredictionService):

    prediction_out = prediction_service.create(prediction_model)
    prediction_saved = Prediction.query.filter(Prediction.id == prediction_model.id).first()

    assert prediction_saved is not None
    assert prediction_out is not None
    assert prediction_saved == prediction_out
    assert prediction_out == prediction_model


@pytest.mark.prediction
def test_prediction_service_read(prediction_model: Prediction, prediction_service: PredictionService):

    prediction_service.create(prediction_model)
    prediction_out = prediction_service.read_by_id(prediction_model.id)

    assert prediction_out is not None
    assert prediction_out == prediction_model


@pytest.mark.prediction
def test_prediction_service_update(prediction_model: Prediction, prediction_service: PredictionService):

    prediction_service.create(prediction_model)

    prediction_model.qid = 'updated qid'
    prediction_out = prediction_service.update(prediction_model)

    assert prediction_out is not None
    assert prediction_out == prediction_model