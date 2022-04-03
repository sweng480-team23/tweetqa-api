from dependency_injector.wiring import inject, Provide
from containers import Container
from controllers.v2 import AbstractCreateReadControllerV2
from dtos.v2.training_dto_v2 import TrainingCreateRequestV2
from dtos.v2.training_dto_v2 import NewTrainingResponseV2
from dacite import from_dict


class TrainingView(AbstractCreateReadControllerV2):

    @inject
    def __init__(
            self,
            account_service=Provide[Container.account_service],
            training_service=Provide[Container.training_service],
            visitor_service=Provide[Container.visitor_service]
    ):
        self.account_service = account_service
        super().__init__(
            service=training_service,
            visitor_service=visitor_service,
            response_dto=NewTrainingResponseV2,
            request_dto=TrainingCreateRequestV2)

    def post(self, request: dict) -> NewTrainingResponseV2:
        # TODO: Check admin auth and get Admin Account info for Creation
        dto: TrainingCreateRequestV2 = from_dict(data_class=self.request_dto, data=request)
        response, status = self.service.create(dto.to_model())
        return NewTrainingResponseV2(message=response), status
