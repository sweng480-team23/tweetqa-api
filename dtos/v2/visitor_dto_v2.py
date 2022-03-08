import abc
from typing import Type, Optional, List
from dataclasses import dataclass
from models.visitor_model import Visitor
from dtos.v2.abstract.abstract_response_v2 import AbstractResponseV2


@dataclass
class VisitorCreateRequestV2(object):
    invitor_account: int
    emails: List[str]

    def to_model(self) -> List[Visitor]:
        return [Visitor(invitor_account=self.invitor_account, email=email) for email in self.emails]


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


@dataclass()
class VisitorCollectionResponseV2(AbstractResponseV2):
    data: List[VisitorResponseV2]

    @staticmethod
    def from_model(models: List[Visitor]) -> List:
        return VisitorCollectionResponseV2(
            data=[VisitorResponseV2(id=m.id, token=m.token) for m in models]
        )
    

@dataclass
class VisitorEnforcedRequest(object):
    visitor: Optional[VisitorResponseV2]

    @abc.abstractmethod
    def to_model(self) -> Type:
        pass
