from dataclasses import dataclass
from typing import List
from models import DataModel
import datetime

@dataclass(frozen=True)
class DataResponse(object):
    qid: str
    tweet: str
    question: str
    answer: str
    created_date: datetime
    updated_date: datetime
    original: str
    start_position: int
    end_position: int

@dataclass(frozen=True)
class DataCreateRequest(object):
    tweet: str
    question: str
    answer: str

    def to_model(self):
        return DataModel(
            tweet = self.tweet,
            question = self.question,
            answer = self.answer,
            created_date = datetime.now()
        )

@dataclass(frozen=True)
class DataCollectionResponse(object):
    # todo - inherit from CollectionResponse base class
    collection: List[DataResponse]