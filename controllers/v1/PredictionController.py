from dtos.v1.PredictionDTOs import PredictionCreateRequest
from services.PredictionService import PredictionService
from dtos.v1.PredictionDTOs import *

prediction_service = PredictionService()


def create_predition(request: dict) -> PredictionResponse:
    '''Controller function to process a create prediction request'''

    dto = PredictionCreateRequest(request)

    try:
        model = prediction_service.create_prediction(dto.to_model())
        response = PredictionResponse(model)
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

def update_prediction(request: dict):
    '''Controller function used to record a corrected answer'''

    dto = PredictionUpdateRequest(request)
    predicition = prediction_service.update_prediction(dto.to_model())
    response = PredictionResponse(predicition)

    return response, 200