from dataclasses import dataclass
import uuid
from dtos.v2.abstract.abstract_response_v2 import AbstractResponseV2
from models.account_model import Account

@dataclass
class AccountLoginRequestV2(object):
    email:str
    password:str

@dataclass
class AccountLoginResponseV2(AbstractResponseV2):
    email:str
    token:str
    expiresIn:str
    @staticmethod
    def from_model(model: Account):
        return AccountLoginResponseV2(
            email = model.email,
            token = uuid.uuid4(),
            expiresIn = '3600'
        )
