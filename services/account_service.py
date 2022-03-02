from sqlalchemy.sql.expression import null
from models.account_model import Account
import string
from services.create_read_update_service import CreateReadUpdateService


class AccountService(CreateReadUpdateService):
    """ AccountService, functions inherited from CreateReadUpdateService : read_by_id(id), create(entity_model), update(entity_model) """

    def __init__(self):
        '''Constructor, take in the specific model class and pass the db.model back to the parent'''
        super().__init__(Account)

    #login function
    #check if the username and password combination exist in the database
    #if not, return null object TODO: need to hash/salt passwords
    def login(self, email: string, password: string) -> Account:
        login_user = Account.query.filter(Account.email==email).first()
        if login_user is None:
            return null
        elif login_user.password == password:
            return login_user
        return null


# def uuid_generator(size : int = 60) -> str:
#     chars = string.ascii_lowercase + string.digits
#     uuid = ''.join(random.choice(chars) for i in range(size))
#     return uuid
#End of AccountService Class
