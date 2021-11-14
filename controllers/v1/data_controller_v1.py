from datetime import datetime
from dtos.v1.data_dto_v1 import DataCollectionResponse, DataCreateRequest, DataResponse
from services.DataService import DataService
import datetime

data_service = DataService()

def create_data(request: dict) -> DataResponse:
    '''Controller function to process a datum create request'''

    req_dto = DataCreateRequest(request)
    req_model = data_service.create_data(req_dto.to_model())
    response = DataResponse(req_model)
    return response, 200

def read_data(qid: str) -> DataResponse:
    '''Controller function to retrieve a datum from a given qid'''

    datum_model = data_service.read_data_by_qid(qid)

    if (datum_model is not None):
        response = DataResponse(datum_model)
        return response, 200

    return qid, 404

def read_all_data_since(date: datetime) -> DataCollectionResponse:
    # todo
    pass

def read_last_x_datum(x: int) -> DataCollectionResponse:
    # todo
    pass

def update_data(updates: DataCollectionResponse) -> DataCollectionResponse:
    # todo
    pass
