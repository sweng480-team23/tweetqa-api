from models import Visitor
from models import Account
from .abstract.create_read_update_service import CreateReadUpdateService
from services import AccountService
import string
from uuid import uuid4
from decouple import config
from typing import List
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import sys


class VisitorService(CreateReadUpdateService):
    """ VisitorService:
        functions inherited from CreateReadUpdateService : read_by_id(id), create(entity_model), update(entity_model) 
        additional functions: def visitor_check (self, token: string) -> Visitor"""   

    def __init__(self):
        """ Constructor, take in the specific model class and pass the db.model back to the parent """
        super().__init__(Visitor)
        self.test_flag = False
        self.account_service = AccountService()

    def create(self, visitors: List[Visitor]) -> List[Visitor]:
        return [self._create(v) for v in visitors]

    def _create(self, visitor: Visitor) -> Visitor:
        visitor.token = str(uuid4())
        created: Visitor = super().create(visitor)

        if 'pytest' not in sys.argv[0]:
            self.email_link(created)

        return created

    def read_by_token(self, token: string) -> Visitor:
        return Visitor.query.filter(Visitor.token == token).first()

    def check_valid_visitor(self, token: string) -> bool:
        """ check if the token is valid """
        if self.read_by_token(token) is None:
            return False
        return True

    def email_link(self, visitor: Visitor):
        message: Mail = Mail(
            from_email='psu.tweetqa@gmail.com',
            to_emails=visitor.email,
            subject="Welcome to TweetQA!",
            html_content=f"""<strong>
                Welcome to TweetQA! Follow this link to interact with our ML models via our Web Application. 
                https://tweetqa-338418.uc.r.appspot.com/?token={visitor.token}</strong>"""
        )
        sg = SendGridAPIClient(api_key=config('SENDGRID_API_KEY'))
        sg.send(message)

    def set_test_flag(self, flag=True):
        self.set_test_flag = flag
