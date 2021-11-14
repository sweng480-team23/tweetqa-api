from dataclasses import dataclass
from string import ascii_letters
import string
from typing import List
import uuid
from models.DataModel import Data
import random
from datetime import datetime

@dataclass
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

    def __init__(self, model: Data):
        '''Constructor to build datum response DTO from a datum model object'''

        self.qid = model.qid
        self.tweet = model.tweet
        self.question = model.question
        self.answer = model.answer
        self.created_date = model.created_date
        self.updated_date = model.updated_date
        self.source = model.source
        self.start_position = model.start_position
        self.end_position = model.end_position
        super().__setattr__('frozen', True)

@dataclass
class DataCreateRequest(object):
    tweet: str
    question: str
    answer: str

    def __init__(self, request: dict):
        '''Constructor to build datum create request DTO from request dictionary'''

        self.tweet = request["tweet"]
        self.question = request["question"]
        self.answer = request["answer"]
        super().__setattr__('frozen', True)

    def to_model(self) -> Data:
        '''Utility function to convert this DTO into a model'''

        return Data(
            qid = ''.join(random.choice(ascii_letters + string.digits) for _ in range(35)),
            tweet = self.tweet,
            question = self.question,
            answer = self.answer,
            created_date = datetime.now(),
            updated_date = datetime.now(),
            source = "sweng480"
        )

@dataclass
class DataCollectionResponse(object):
    # todo - inherit from CollectionResponse base class
    collection: List[DataResponse]