from datetime import datetime
from dtos.v1.data_dto_v1 import DataCollectionResponse, DataCreateRequest, DataResponse
from services.DataService import DataService
import datetime

data_service = DataService()

def create_data(request: DataCreateRequest) -> DataResponse:
    req_model = data_service.create_data(request.to_model())
    return req_model, 200

def read_data(qid: str) -> DataResponse:
    datum = data_service.read_data_by_qid(qid)
    if (datum):
        return datum, 200

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
