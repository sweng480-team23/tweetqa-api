from typing import Type
from services import CreateReadUpdateService
from services import VisitorService
from controllers.v2 import AbstractCreateReadControllerV2
from dtos.v2.abstract import AbstractResponseV2
from dtos.v2 import VisitorEnforcedRequest
from dacite import from_dict


class AbstractCreateReadUpdateControllerV2(AbstractCreateReadControllerV2):

    def __init__(
            self,
            service: CreateReadUpdateService,
            visitor_service: VisitorService,
            response_dto: Type[AbstractResponseV2],
            request_dto: Type[VisitorEnforcedRequest],
            update_request_dto: Type[VisitorEnforcedRequest]
    ):
        super().__init__(service, visitor_service, response_dto, request_dto)
        self.service = service
        self.update_request_dto = update_request_dto

    def put(self, resource_id: int, request: dict):
        """ /v2/{resource}/{resource_id} """
        dto = from_dict(data_class=self.update_request_dto, data=request)
        if self.visitor_service.check_valid_visitor(dto.visitor.token):
            resource = self.service.update(dto.to_model())
            response = self.response_dto.from_model(resource)
            return response, 200
        else:
            return None, 403
