from sqlalchemy.sql.expression import null
from controllers import db
from models.account_model import Account
from models.visitor_model import Visitor
import string, uuid
from services.create_read_update_service import CreateReadUpdateService
from services.visitor_service import VisitorService

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

    def generate_token_invitation_for_email(self, email:string)->Visitor:
        new_token = uuid.uuid4()
        new_visitor = Visitor(
            token = new_token,
            email = email,
            invitor_account = 1
            #TODO - to fetch the invitor_account information somehow from the controller
        )
        saved_visitor = VisitorService().create(new_visitor)
        return saved_visitor
        #to be implemented

# def uuid_generator(size : int = 60) -> str:
#     chars = string.ascii_lowercase + string.digits
#     uuid = ''.join(random.choice(chars) for i in range(size))
#     return uuid
#End of AccountService Class
