from models import Visitor
from models import Account
from .abstract.create_read_update_service import CreateReadUpdateService
from services import AccountService
import string
from uuid import uuid4
import smtplib
import ssl
from email.message import EmailMessage
from decouple import config
from typing import List


class VisitorService(CreateReadUpdateService):
    """ VisitorService:
        functions inherited from CreateReadUpdateService : read_by_id(id), create(entity_model), update(entity_model) 
        additional functions: def visitor_check (self, token: string) -> Visitor"""   

    def __init__(self):
        """ Constructor, take in the specific model class and pass the db.model back to the parent """
        super().__init__(Visitor)
        self.account_service = AccountService()

    def create(self, visitors: List[Visitor]) -> List[Visitor]:
        return [self._create(v) for v in visitors]

    def _create(self, visitor: Visitor) -> Visitor:
        visitor.token = str(uuid4())
        created: Visitor = super().create(visitor)
        #self.email_link(created)
        return created

    def read_by_token(self, token: string) -> Visitor:
        return Visitor.query.filter(Visitor.token == token).first()

    def check_valid_visitor(self, token: string) -> bool:
        """ check if the token is valid """
        if self.read_by_token(token) is None:
            return False
        return True

    def email_link(self, visitor: Visitor):
        invitor: Account = self.account_service.read_by_id(visitor.invitor_account)
        msg = EmailMessage()
        msg.set_content(
            f"""Welcome to TweetQA! Follow this link to interact with our ML models via our Web Application.

            localhost:8080?token={visitor.token}""")
        msg['Subject'] = "Welcome to TweetQA!"
        msg['From'] = invitor.email
        msg['To'] = visitor.email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login('psu.tweetqa@gmail.com', config('GMAIL_PWD'))
            server.send_message(msg)
            server.quit()
