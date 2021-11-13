from dtos.v1.QAModelDTOs import QAModelCreateRequest, QAModelResponse
from dtos.v1.WordCloudDTOs import WordCloudRequest, WordCloudResponse
from models import QAModel
from services.QAModelService import QAModelService
from datetime import datetime


qa_model_service = QAModelService()


# TODO: Add the end point to drive this method
def create_qa_model(request: QAModelCreateRequest) -> QAModelResponse:
    '''Controller function to process a model create request'''


    model = request.to_model()

    try:
        model = qa_model_service.create_qa_model(model)
        response = QAModelResponse(model)
        return response, 200

    except Exception as e:
        print(e)
        return None, 404



def read_qa_model(uuid: str) -> QAModelResponse:
    '''Controller function to get a given model based on uuid'''

    model = qa_model_service.read_qa_model_by_uuid(uuid)

    # Model is found and return the DTO or return None
    if model is not None:
        response = QAModelResponse(model)
        return response, 200
    else:
        return None, 404


def read_latest_qa_model_by_type(model_type: str) -> QAModelResponse:
    '''Controller function to return the latest model by type'''

    model = qa_model_service.read_latest_qa_model_by_type(model_type)

    # Model is found and return the DTO or return None
    if model is not None:
        response = QAModelResponse(model)
        return response, 200
    else:
        return None, 404


def get_word_cloud(request: WordCloudRequest) -> WordCloudResponse:
    '''Controller function to get the latest wordcloud'''

    raise NotImplementedError
