from dataclasses import dataclass

from models import Prediction
from dtos.v1.QAModelDTOs import QAModelResponse


@dataclass
class PredictionCreateRequest(object):
    token: str
    model_id: str
    prediction: str
    
    #TODO: Add Datum class
    
    
    def to_model(self) -> Prediction: 
        return Prediction(token=self.token,
                                model_id=self.model_id,
                                prediction=self.prediction) 

        


@dataclass
class PredictionUpdateRequest(object):
    id: int
    is_corrected: bool
    alt_answer: str

    def to_model(self) -> Prediction:
        return Prediction(id=self.id,
                          is_corrected=self.is_corrected,
                          alt_answer=self.alt_answer)


@dataclass
class PredictionResponse(object):
    id: int
    token: str
    prediction: str
    is_corrected: bool
    alt_answer: str
    model: QAModelResponse
    #TODO: add the datum class

    def __init__(self, prediction: Prediction) -> None:
        self.id = prediction.id
        self.token = prediction.visitor.token
        self.prediction = prediction.prediction
        self.is_corrected = prediction.is_corrected
        self.alt_answer = prediction.alt_answer
        self.model = QAModelResponse(prediction.model)
