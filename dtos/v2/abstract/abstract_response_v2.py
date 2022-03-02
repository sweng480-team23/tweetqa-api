import abc
from dataclasses import dataclass
from typing import TypeVar

MODEL = TypeVar("MODEL")
RESPONSE = TypeVar("RESPONSE")


@dataclass
class AbstractResponseV2(object):

    @staticmethod
    @abc.abstractmethod
    def from_model(model: MODEL) -> RESPONSE:
        pass
