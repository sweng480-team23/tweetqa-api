from dtos.v1.PredictionDTOs import PredictionCreateRequest
from services.PredictionService import PredictionService
from dtos.v1.PredictionDTOs import *

prediction_service = PredictionService()


def create_predition(request: dict) -> PredictionResponse:
    '''Controller function to process a create prediction request'''

    dto = PredictionCreateRequest(request)
    prediction_service.create_prediction(dto.to_model(), dto.model_id)


    raise NotImplementedError

def update_prediction(update: dict):
    raise NotImplementedError