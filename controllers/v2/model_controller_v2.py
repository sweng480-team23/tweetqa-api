from dependency_injector.wiring import inject, Provide
from containers import Container
from typing import List
from tqatypes.word_response import WordResponse
from services import VisitorService
from services import QAModelService
from services import DataService
from controllers.v2 import AbstractCreateReadControllerV2
from dtos.v2 import QAModelResponseV2
from dtos.v2 import QAModelCreateRequestV2
from dtos.v2 import WordCloudResponseV2


class ModelsView(AbstractCreateReadControllerV2):

    @inject
    def __init__(
            self,
            visitor_service: VisitorService = Provide[Container.visitor_service],
            model_service: QAModelService = Provide[Container.model_service],
            data_service: DataService = Provide[Container.data_service]
    ):
        super().__init__(
            service=model_service,
            visitor_service=visitor_service,
            response_dto=QAModelResponseV2,
            request_dto=QAModelCreateRequestV2
        )
        self.data_service = data_service

    def get_word_cloud(self, resource_id: str) -> WordCloudResponseV2:
        word_cloud: List[WordResponse] = self.data_service.generate_word_cloud(resource_id)
        if len(word_cloud) > 0:
            return WordCloudResponseV2(resource_id, word_cloud), 200
        else:
            return None, 404
