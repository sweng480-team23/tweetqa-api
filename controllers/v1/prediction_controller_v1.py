from dtos.v1.prediction_dto_v1 import PredictionCreateRequest
from services.prediction_service import PredictionService
from dtos.v1.prediction_dto_v1 import *

prediction_service = PredictionService()


def create_prediction(request: dict) -> PredictionResponse:
    '''Controller function to process a create prediction request'''

    dto = PredictionCreateRequest(request)
    try:
        prediction: Prediction = prediction_service.create(dto.to_model())
        response = PredictionResponse(prediction)
        return response, 200

    except Exception as e:
        print(e)
        return None, 404


def read_prediction(id_: int) -> PredictionResponse:
    '''Controller function to process prediciton read request by id'''

    prediciton = prediction_service.read_prediciton_by_id(id_)

    if prediciton is not None:
        response = PredictionResponse(prediciton)
        return response, 200
    else:
        return None, 404


def update_prediction(id_: int, request: dict):
    '''Controller function used to record a corrected answer'''

    dto = PredictionUpdateRequest(request)
    predicition = prediction_service.update(dto.to_model())
    response = PredictionResponse(predicition)

    return response, 200