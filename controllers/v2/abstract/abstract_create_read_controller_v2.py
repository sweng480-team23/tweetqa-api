from typing import Type
from services import CreateReadService
from services import VisitorService
from controllers.v2 import AbstractReadControllerV2
from dtos.v2.abstract import AbstractResponseV2
from dtos.v2 import VisitorEnforcedRequest
from dacite import from_dict


class AbstractCreateReadControllerV2(AbstractReadControllerV2):

    def __init__(
            self,
            service: CreateReadService,
            visitor_service: VisitorService,
            response_dto: Type[AbstractResponseV2],
            request_dto: Type[VisitorEnforcedRequest]
    ):
        super().__init__(service, response_dto)
        self.service = service
        self.visitor_service = visitor_service
        self.request_dto = request_dto

    def post(self, request: dict):
        """ /v2/{resource} """
        dto: Type[VisitorEnforcedRequest] = from_dict(data_class=self.request_dto, data=request)
        if dto.visitor is not None and self.visitor_service.check_valid_visitor(dto.visitor.token):
            try:
                resource = self.service.create(dto.to_model())
                response = self.response_dto.from_model(resource)
                return response, 200
            except Exception as e:
                print(e)
                return None, 404
        else:
            return None, 403
