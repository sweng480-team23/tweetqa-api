from dataclasses import dataclass
from datetime import datetime
from models.QAModel import QAModel

@dataclass(frozen=True)
class QAModelCreateRequest(object):
    ml_type: str
    ml_version: str
    bleu_score: float
    rouge_score: float
    meteor_score: float

    def to_model(self) -> QAModel:
        return QAModel(ml_type=self.ml_type, 
                        ml_version=self.ml_version,
                        bleu_score=self.bleu_score,
                        rouge_score=self.rouge_score,
                        meteor_score=self.meteor_score,
                        created=datetime.now())

@dataclass(frozen=True)
class QAModelResponse(object):
    model_uuid: str
    created: datetime
    ml_type: str
    ml_version: str
    bleu_score: float
    rouge_score: float
    meteor_score: float



     