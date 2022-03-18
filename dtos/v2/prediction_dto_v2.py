from dataclasses import dataclass
from models import Prediction
from dtos.v2.abstract import AbstractResponseV2
from dtos.v2 import VisitorResponseV2
from dtos.v2 import VisitorEnforcedRequest
from dtos.v2 import PartialDataResponseV2
from dtos.v2 import DataCreateRequestV2


@dataclass
class PredictionCreateRequestV2(VisitorEnforcedRequest):
    model_id: str
    datum: DataCreateRequestV2

    def to_model(self) -> Prediction:
        return Prediction(prediction=self.datum.answer,
                          model_id=self.model_id,
                          datum=self.datum.to_model(),
                          visitor_id=self.visitor.id)


@dataclass
class PredictionUpdateRequestV2(VisitorEnforcedRequest):
    id: int
    is_correct: bool
    alt_answer: str

    def to_model(self) -> Prediction:
        return Prediction(id=self.id,
                          is_correct=self.is_correct,
                          alt_answer=self.alt_answer)


@dataclass
class PredictionResponseV2(AbstractResponseV2):
    id: int
    visitor: VisitorResponseV2
    prediction: str
    is_correct: bool
    alt_answer: str
    # model: QAModelResponse
    datum: PartialDataResponseV2

    @staticmethod
    def from_model(model: Prediction):
        return PredictionResponseV2(
            id=model.id,
            visitor=VisitorResponseV2.from_model(model.visitor),
            prediction=model.prediction,
            is_correct=model.is_correct,
            alt_answer=model.alt_answer,
            # self.model = QAModelResponse(prediction.model)
            datum=PartialDataResponseV2.from_model(model.datum)
        )
