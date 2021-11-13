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
    source: str
    start_position: int
    end_position: int

    def __init__(self, model: DataModel.Data):
        self.qid = model.qid
        self.tweet = model.tweet
        self.question = model.question
        self.answer = model.answer
        self.created_date = model.created_date
        self.updated_date = model.updated_date
        self.source = model.source
        self.start_position = model.start_position

@dataclass(frozen=True)
class DataCreateRequest(object):
    tweet: str
    question: str
    answer: str

    def __init__(self, model: DataModel.Data):
        self.tweet = model.tweet
        self.question = model.question
        self.answer = model.answer

    def to_model(self) -> DataModel.Data:
        return DataModel(
            tweet = self.tweet,
            question = self.question,
            answer = self.answer
        )

@dataclass(frozen=True)
class DataCollectionResponse(object):
    # todo - inherit from CollectionResponse base class
    collection: List[DataResponse]