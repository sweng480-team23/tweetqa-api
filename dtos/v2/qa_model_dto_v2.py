from dataclasses import dataclass
from datetime import datetime
from models import QAModel
from dtos.v2.abstract import AbstractResponseV2
from dtos.v2 import VisitorEnforcedRequest


@dataclass
class QAModelCreateRequestV2(VisitorEnforcedRequest):
    ml_type: str
    ml_version: str
    bleu_score: float
    rouge_score: float
    meteor_score: float
    model_url: str

    def to_model(self) -> QAModel:
        return QAModel( ml_type=self.ml_type,
                        ml_version=self.ml_version,
                        bleu_score=self.bleu_score,
                        rouge_score=self.rouge_score,
                        meteor_score=self.meteor_score,
                        model_url=self.model_url,
                        created_date=datetime.now())


@dataclass
class QAModelResponseV2(AbstractResponseV2):
    id: int
    created_date: datetime
    ml_type: str
    ml_version: str
    bleu_score: float
    rouge_score: float
    meteor_score: float

    @staticmethod
    def from_model(model: QAModel):
        return QAModelResponseV2(
            id=model.id,
            created_date=model.created_date,
            ml_type=model.ml_type,
            ml_version=model.ml_version,
            bleu_score=model.bleu_score,
            rouge_score=model.rouge_score,
            meteor_score=model.meteor_score
        )
