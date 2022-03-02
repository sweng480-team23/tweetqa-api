from dependency_injector.wiring import inject, Provide
from containers import Container
from services.prediction_service import PredictionService
from services.visitor_service import VisitorService
from controllers.v2 import AbstractCreateReadUpdateControllerV2
from dtos.v2 import PredictionCreateRequestV2
from dtos.v2 import PredictionResponseV2
from dtos.v2 import PredictionUpdateRequestV2


class PredictionsView(AbstractCreateReadUpdateControllerV2):

    @inject
    def __init__(
            self,
            visitor_service: VisitorService = Provide[Container.visitor_service],
            prediction_service: PredictionService = Provide[Container.prediction_service]
    ):
        super().__init__(
            service=prediction_service,
            visitor_service=visitor_service,
            response_dto=PredictionResponseV2,
            request_dto=PredictionCreateRequestV2,
            update_request_dto=PredictionUpdateRequestV2
        )
