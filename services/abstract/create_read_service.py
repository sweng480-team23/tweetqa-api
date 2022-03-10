from controllers import db
from .read_service import ReadService


class CreateReadService(ReadService):
    '''basic read class to handle all database Read operations for models'''
    
    '''Constructor, take in the specific model class and pass the db.model back to the parent'''
    def __init__(self, entityModel:db.Model):
        super().__init__(entityModel)
    
    def create(self, data) -> db.Model:
        db.session.add(data)
        db.session.commit()
        saved_data = self.read_by_id(data.id)
        return saved_data
