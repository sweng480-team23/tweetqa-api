import abc
from typing import Type, Optional
from dataclasses import dataclass
from models.visitor_model import Visitor
from dtos.v2.abstract.abstract_response_v2 import AbstractResponseV2


@dataclass
class VisitorCreateRequestV2(object):
    invitor_account: int
    email: str

    def to_model(self) -> Visitor:
        return Visitor(invitor_account=self.invitor_account, email=self.email)


@dataclass
class VisitorResponseV2(AbstractResponseV2):
    id: int
    token: str

    @staticmethod
    def from_model(model: Visitor):
        return VisitorResponseV2(
            id=model.id,
            token=model.token
        )


@dataclass
class VisitorEnforcedRequest(object):
    visitor: Optional[VisitorResponseV2]

    @abc.abstractmethod
    def to_model(self) -> Type:
        pass
