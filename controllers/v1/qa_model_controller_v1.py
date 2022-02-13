from dtos.v1.qa_model_dto_v1 import QAModelCreateRequest, QAModelResponse
from dtos.v1.word_cloud_dto_v1 import WordCloudResponse, WordResponse
from dtos.v1.collection_dto_v1 import CollectionDTOResponse
from services.qa_model_service import QAModelService
from services.data_service import DataService
from models.qa_model import QAModel
from typing import List


qa_model_service = QAModelService()
data_service = DataService()


def create_qa_model(request: dict) -> QAModelResponse:
    '''Controller function to process a model create request'''

    dto = QAModelCreateRequest(request)
    model = dto.to_model()

    try:
        #model = qa_model_service.create_qa_model(model)
        model = qa_model_service.create(model)
        response = QAModelResponse(model)
        return response, 200

    except Exception as e:
        print(e)
        return None, 404


def read_qa_model(id_: str) -> QAModelResponse:
    '''Controller function to get a given model based on id'''

    #model = qa_model_service.read_qa_model_by_id(id_)
    #watch for passing in str instead of int
    model = qa_model_service.read_by_id(id_)

    # Model is found and return the DTO or return None
    if model is not None:
        response = QAModelResponse(model)
        return response, 200
    else:
        return None, 404


def read_all_qa_model_by_type(model_type: str) -> List[QAModelResponse]:
    models: List[QAModel] = qa_model_service.read_all_qa_model_by_type(model_type)

    if len(models) > 0:
        return [QAModelResponse(model) for model in models], 200
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


def read_latest_models() -> CollectionDTOResponse:
    models = qa_model_service.read_latest_models()

    response = CollectionDTOResponse()
    for model in models:
        response.add(QAModelResponse(model))

    return response, 200


def get_word_cloud(id_: str) -> WordCloudResponse:
    '''Controller function to get the latest wordcloud'''
    word_cloud: List[WordResponse] = data_service.generate_word_cloud(id_)
    if len(word_cloud) > 0:
        return WordCloudResponse(id_, word_cloud), 200
    else:
        return None, 404
