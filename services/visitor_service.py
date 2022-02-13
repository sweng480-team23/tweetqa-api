from controllers import db
from models.visitor_model import Visitor
from services.create_read_update_service import CreateReadUpdateService
import string
from sqlalchemy.sql.expression import null

class VisitorService(CreateReadUpdateService):
    """ VisitorService:
        functions inherited from CreateReadUpdateService : read_by_id(id), create(entity_model), update(entity_model) 
        additional functions: def visitor_check (self, token: string) -> Visitor"""   

    def __init__(self):
        '''Constructor, take in the specific model class and pass the db.model back to the parent'''
        super().__init__(Visitor)



    def visitor_check (self, token: string) -> Visitor:
        '''check if the token valid and return the visitor information '''
        checkin_user = Visitor.query.filter(Visitor.token==token).first()
        if checkin_user is None:
            return null
        return checkin_user