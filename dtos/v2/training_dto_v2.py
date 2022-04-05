from dataclasses import dataclass
from dtos.v2.abstract.abstract_dto_v2 import AbstractRequestV2
from dtos.v2.abstract.abstract_dto_v2 import AbstractResponseV2
from dtos.v2.account_dto_v2 import AccountLoginResponseV2
from models.training_model import Training
from datetime import datetime


@dataclass
class TrainingCreateRequestV2(AbstractRequestV2):
    admin: AccountLoginResponseV2
    epochs: int
    learningRate: str
    batchSize: int
    baseModel: str
    lastXLabels: int
    includeUserLabels: bool

    def to_model(self) -> Training:
        return Training(
            created=datetime.now(),
            epochs=self.epochs,
            learningRate=self.learningRate,
            batchSize=self.batchSize,
            baseModel=self.baseModel,
            lastXLabels=self.lastXLabels,
            includeUserLabels=self.includeUserLabels,
        )


@dataclass
class NewTrainingResponseV2(object):
    message: str


@dataclass
class TrainingResponseV2(AbstractResponseV2):
    id: int
    admin: AccountLoginResponseV2
    epochs: int
    learningRate: str
    batchSize: int
    baseModel: str
    lastXLabels: int
    includeUserLabels: bool

    @staticmethod
    def from_model(model: Training):
        return TrainingResponseV2(
            id=model.id,
            admin=AccountLoginResponseV2.from_model(model.admin),
            epochs=model.epochs,
            learningRate=model.learningRate,
            batchSize=model.batchSize,
            baseModel=model.baseModel,
            lastXLabels=model.lastXLabels,
            includeUserLabels=model.includeUserLabels,
        )
