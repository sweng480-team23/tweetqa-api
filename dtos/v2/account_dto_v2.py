

from dataclasses import dataclass
import uuid

from models.account_model import Account


@dataclass
class AccountLoginRequestV2(object):
    email:str
    password:str

    def __init__(self, request: dict) -> None:
        self.email = request["email"]
        self.password = request["password"]
        super().__setattr__('frozen', True)

@dataclass
class AccountLoginResponseV2(object):
    email:str
    token:str
    expiresIn:str

    def __init__(self, account:Account) -> None:
        self.email = account.email
        self.token = uuid.uuid4()
        self.expiresIn = '3600'
