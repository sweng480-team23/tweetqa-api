from sqlalchemy.sql.expression import null
from models import Account
import string
from .abstract.create_read_update_service import CreateReadUpdateService


class AccountService(CreateReadUpdateService):
    """ AccountService, functions inherited from CreateReadUpdateService : read_by_id(id), create(entity_model), update(entity_model) """

    def __init__(self):
        '''Constructor, take in the specific model class and pass the db.model back to the parent'''
        super().__init__(Account)

    def get_by_email(self, email) -> Account:
        return Account.query.filter(Account.email == email).first()

    #login function
    #check if the username and password combination exist in the database
    #if not, return null object TODO: need to hash/salt passwords
    def login(self, email: string, password: string) -> Account:
        login_user = self.get_by_email(email)
        if login_user is None:
            return null
        elif login_user.password == password:
            return login_user
        return null
