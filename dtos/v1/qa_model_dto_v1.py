from dataclasses import dataclass
from datetime import datetime
from models import QAModel


@dataclass
class QAModelCreateRequest(object):
    ml_type: str
    ml_version: str
    bleu_score: float
    rouge_score: float
    meteor_score: float

    def __init__(self, request: dict) -> None:
        '''Constructor to build model from request dictionary'''

        self.ml_type = request["ml_type"]
        self.ml_version = request["ml_version"]
        self.bleu_score = request["bleu_score"]
        self.rouge_score = request["rouge_score"]
        self.meteor_score = request["meteor_score"]
        super().__setattr__('frozen', True)

    def to_model(self) -> QAModel:
        '''Utility function to convert this DTO into a model'''

        return QAModel( ml_type=self.ml_type, 
                        ml_version=self.ml_version,
                        bleu_score=self.bleu_score,
                        rouge_score=self.rouge_score,
                        meteor_score=self.meteor_score,
                        created_date=datetime.now())


@dataclass
class QAModelResponse(object):

    id: int
    created_date: datetime
    ml_type: str
    ml_version: str
    bleu_score: float
    rouge_score: float
    meteor_score: float

    def __init__(self, model: QAModel) -> None:
        '''Constructor to build response from model'''

        self.id = model.id
        self.created_date = model.created_date
        self.ml_type = model.ml_type
        self.ml_version = model.ml_version
        self.bleu_score = model.bleu_score
        self.rouge_score = model.rouge_score
        self.meteor_score = model.meteor_score
        super().__setattr__('frozen', True)
