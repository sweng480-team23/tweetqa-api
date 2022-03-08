from models import Visitor
from services.visitor_service import VisitorService
from dtos.v2.visitor_dto_v2 import VisitorCreateRequestV2
from dtos.v2.visitor_dto_v2 import VisitorResponseV2
from dtos.v2.visitor_dto_v2 import VisitorCollectionResponseV2
from controllers.v2 import AbstractReadControllerV2
from dependency_injector.wiring import inject, Provide
from containers import Container
from dacite import from_dict


class VisitorsView(AbstractReadControllerV2):
    """ /v2/visitors """

    @inject
    def __init__(self, visitor_service: VisitorService = Provide[Container.visitor_service]):
        super().__init__(visitor_service, VisitorResponseV2)
        self.visitor_service = visitor_service

    def get_by_token(self, token: str) -> VisitorResponseV2:
        visitor: Visitor = self.visitor_service.read_by_token(token)
        if visitor:
            return VisitorResponseV2.from_model(visitor), 200
        else:
            return None, 404

    def post(self, request: dict) -> VisitorCollectionResponseV2:
        dto: VisitorCreateRequestV2 = from_dict(data_class=VisitorCreateRequestV2, data=request)
        return VisitorCollectionResponseV2.from_model(
            self.visitor_service.create(dto.to_model())), 200
