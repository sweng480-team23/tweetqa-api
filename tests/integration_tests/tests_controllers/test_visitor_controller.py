from dataclasses import dataclass
from models.prediction_model import Prediction
from dtos.v2.qa_model_dto_v2 import QAModelResponseV2
from dtos.v2.data_dto_v2 import DataCreateRequestV2, DataResponseV2
from dtos.v2.visitor_dto_v2 import VisitorResponseV2


@dataclass
class PredictionCreateRequestV2(object):
    model_id: int
    datum: DataCreateRequestV2
    visitor: VisitorResponseV2

    def to_model(self) -> Prediction:
        return Prediction(prediction=self.datum.answer,
                          model_id=self.model_id,
                          datum=self.datum.to_model(),
                          visitor_id=self.visitor.id)


@dataclass
class PredictionUpdateRequestV2(object):
    id: int
    is_correct: bool
    alt_answer: str
    visitor: VisitorResponseV2

    def to_model(self) -> Prediction:
        return Prediction(id=self.id,
                          is_correct=self.is_correct,
                          alt_answer=self.alt_answer)


@dataclass
class PredictionResponseV2(object):
    id: int
    visitor: VisitorResponseV2
    prediction: str
    is_correct: bool
    alt_answer: str
    model: QAModelResponseV2
    datum: DataResponseV2

    def __init__(self, prediction: Prediction):
        self.id = prediction.id
        self.visitor = VisitorResponseV2(prediction.visitor)
        self.prediction = prediction.prediction
        self.is_correct = prediction.is_correct
        self.alt_answer = prediction.alt_answer
        # self.model = QAModelResponse(prediction.model)
        self.model = None
        self.datum = DataResponseV2(prediction.datum)
