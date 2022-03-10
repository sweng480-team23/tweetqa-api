from dataclasses import dataclass
from models.prediction_model import Prediction
from dtos.v1.qa_model_dto_v1 import QAModelResponse
from dtos.v1.data_dto_v1 import DataCreateRequest, DataResponse
from dtos.v1.visitor_dto_v2 import VisitorResponseV2


@dataclass
class PredictionCreateRequestV2(object):
    model_id: int
    datum: DataCreateRequest
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
    model: QAModelResponse
    datum: DataResponse

    def __init__(self, prediction: Prediction):
        self.id = prediction.id
        self.visitor = VisitorResponseV2(prediction.visitor)
        self.prediction = prediction.prediction
        self.is_correct = prediction.is_correct
        self.alt_answer = prediction.alt_answer
        # self.model = QAModelResponse(prediction.model)
        self.model = None
        self.datum = DataResponse(prediction.datum)
