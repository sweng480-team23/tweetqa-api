from dataclasses import dataclass
from datetime import datetime
from models.QAModel import QAModel
import uuid

@dataclass(frozen=True)
class QAModelCreateRequest(object):
    ml_type: str
    ml_version: str
    bleu_score: float
    rouge_score: float
    meteor_score: float

    def to_model(self) -> QAModel:
        return QAModel( uuid=str(uuid.uuid1()),
                        ml_type=self.ml_type, 
                        ml_version=self.ml_version,
                        bleu_score=self.bleu_score,
                        rouge_score=self.rouge_score,
                        meteor_score=self.meteor_score,
                        created=datetime.now())

@dataclass()
class QAModelResponse(object):

    uuid: str
    created_date: datetime
    ml_type: str
    ml_version: str
    bleu_score: float
    rouge_score: float
    meteor_score: float

    def __init__(self, model: QAModel):
        self.uuid = model.uuid
        self.created_date = model.created_date
        self.ml_type = model.ml_type
        self.ml_version = model.ml_version
        self.bleu_score = model.bleu_score
        self.rouge_score = model.rogue_score
        self.meteor_score = model.meteor_score
        super().__setattr__('Frozen', True)

     