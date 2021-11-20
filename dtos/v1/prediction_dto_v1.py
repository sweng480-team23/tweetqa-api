from dataclasses import dataclass

from models import Prediction
from dtos.v1.qa_model_dto_v1 import QAModelResponse
from dtos.v1.data_dto_v1 import DataCreateRequest, DataResponse


@dataclass
class PredictionCreateRequest(object):
    token: str
    model_id: str
    datum: DataCreateRequest

    def __init__(self, request: dict) -> None:
        self.token = request["token"]
        self.model_id = request["model_id"]
        self.datum = DataCreateRequest(request["datum"])
        super().__setattr__('frozen', True)


    #TODO: Work around for the token
    def to_model(self) -> Prediction:
        return Prediction(prediction=self.datum.answer,
                          model_id=self.model_id,
                          datum=self.datum.to_model(),
                          visitor_id=1)


@dataclass
class PredictionUpdateRequest(object):
    id: int
    is_correct: bool
    alt_answer: str

    def __init__(self, update: dict) -> None:
        self.id = update["id"]
        self.is_correct = update["is_correct"]
        self.alt_answer = update["alt_answer"]

    def to_model(self) -> Prediction:
        return Prediction(id=self.id,
                          is_correct=self.is_correct,
                          alt_answer=self.alt_answer)


@dataclass
class PredictionResponse(object):
    id: int
    token: str
    prediction: str
    is_correct: bool
    alt_answer: str
    model: QAModelResponse
    datum: DataResponse

    def __init__(self, prediction: Prediction) -> None:
        self.id = prediction.id
        self.token = prediction.visitor.token
        self.prediction = prediction.prediction
        self.is_correct = prediction.is_correct
        self.alt_answer = prediction.alt_answer
        self.model = QAModelResponse(prediction.model)
        self.datum = DataResponse(prediction.datum)
