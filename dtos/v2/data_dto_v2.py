from dataclasses import dataclass
from string import ascii_letters
import string
from typing import List, Optional
from models.data_model import Data
import random
from datetime import datetime
from dtos.v2.abstract import AbstractResponseV2
from dtos.v2 import VisitorEnforcedRequest


@dataclass
class DataResponseV2(AbstractResponseV2):
    qid: str
    tweet: str
    question: str
    answer: str
    created_date: datetime
    updated_date: datetime
    source: str
    start_position: int
    end_position: int

    @staticmethod
    def from_model(model: Data):
        return DataResponseV2(
            qid=model.qid,
            tweet=model.tweet,
            question=model.question,
            answer=model.answer,
            created_date=model.created_date,
            updated_date=model.updated_date,
            source=model.source,
            start_position=model.start_position,
            end_position=model.end_position
        )


@dataclass
class PartialDataResponseV2(AbstractResponseV2):
    qid: str
    tweet: str
    question: str
    created_date: datetime
    updated_date: datetime

    @staticmethod
    def from_model(model: Data):
        return PartialDataResponseV2(
            qid=model.qid,
            tweet=model.tweet,
            question=model.question,
            created_date=model.created_date,
            updated_date=model.updated_date
        )


@dataclass
class DataCreateRequestV2(VisitorEnforcedRequest):
    tweet: str
    question: str
    answer: Optional[str]

    def to_model(self) -> Data:
        return Data(
            qid=''.join(random.choice(ascii_letters + string.digits) for _ in range(35)),
            tweet=self.tweet,
            question=self.question,
            answer=self.answer,
            created_date=datetime.now(),
            updated_date=datetime.now(),
            source="sweng480"
        )


@dataclass
class DataUpdateRequestV2(VisitorEnforcedRequest):
    qid: str
    answer: Optional[str]
    start_position: Optional[int]
    end_position: Optional[int]

    def to_model(self) -> Data:
        return Data(
            qid=self.qid,
            answer=self.answer,
            start_position=self.start_position,
            end_position=self.end_position
        )


@dataclass
class DataCollectionResponseV2(object):
    # TODO: - inherit from CollectionResponse base class
    collection: List[DataResponseV2]
