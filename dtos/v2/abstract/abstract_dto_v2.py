import abc
from dataclasses import dataclass
from typing import TypeVar, Type

MODEL = TypeVar("MODEL")
RESPONSE = TypeVar("RESPONSE")


@dataclass
class AbstractRequestV2(object):

    @abc.abstractmethod
    def to_model(self) -> Type:
        pass



@dataclass
class AbstractResponseV2(object):

    @staticmethod
    @abc.abstractmethod
    def from_model(model: MODEL) -> RESPONSE:
        pass
