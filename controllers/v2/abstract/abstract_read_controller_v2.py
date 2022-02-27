from flask.views import MethodView
from services import ReadService
from typing import Type
from dtos.v2 import AbstractResponseV2


class AbstractReadControllerV2(MethodView):

    def __init__(self, service: ReadService, response_dto: Type[AbstractResponseV2]):
        self.service = service
        self.response_dto = response_dto

    def get(self, resource_id: int):
        """ /v2/{resource}/{resource_id} """
        resource = self.service.read_by_id(resource_id)
        if resource is not None:
            response = self.response_dto.from_model(resource)
            return response, 200
        else:
            return None, 404
