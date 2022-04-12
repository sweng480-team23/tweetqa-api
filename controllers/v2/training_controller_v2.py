from dependency_injector.wiring import inject, Provide
from containers import Container
from controllers.v2 import AbstractCreateReadControllerV2
from dtos.v2.training_dto_v2 import TrainingCreateRequestV2
from dtos.v2.training_dto_v2 import NewTrainingResponseV2
from dacite import from_dict
from models.training_model import Training


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
        # TODO: Check admin auth
        dto: TrainingCreateRequestV2 = from_dict(data_class=self.request_dto, data=request)
        training_model: Training = dto.to_model()
        training_model.admin = self.account_service.get_by_email(dto.admin.email)
        response, status = self.service.create(training_model)
        return NewTrainingResponseV2(message=response), status
