from dependency_injector.wiring import inject, Provide
from containers import Container
from services import DataService
from services import VisitorService
from controllers.v2 import AbstractCreateReadUpdateControllerV2
from dtos.v2 import DataResponseV2
from dtos.v2 import DataCreateRequestV2
from dtos.v2 import DataUpdateRequestV2


class DataView(AbstractCreateReadUpdateControllerV2):

    @inject
    def __init__(
            self,
            data_service: DataService = Provide[Container.data_service],
            visitor_service: VisitorService = Provide[Container.visitor_service]
     ):
        super().__init__(
            service=data_service,
            visitor_service=visitor_service,
            response_dto=DataResponseV2,
            request_dto=DataCreateRequestV2,
            update_request_dto=DataUpdateRequestV2
        )