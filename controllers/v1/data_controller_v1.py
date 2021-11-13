from datetime import datetime
from ...dtos.v1.data_dto_v1 import DataCollectionResponse, DataCreateRequest, DataResponse
import datetime

def create_data(request: DataCreateRequest) -> DataResponse:
    # todo
    pass

def read_data(qid: int) -> DataResponse:
    # todo
    pass

def read_all_data_since(date: datetime) -> DataCollectionResponse:
    # todo
    pass

def read_last_x_datum(x: int) -> DataCollectionResponse:
    # todo
    pass

def update_data(updates: DataCollectionResponse) -> DataCollectionResponse:
    # todo
    pass
