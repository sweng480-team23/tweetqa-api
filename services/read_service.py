from controllers import db
from sqlalchemy import String, Integer

class ReadService(object):
    '''basic read class to handle all database Read operations for models'''

    '''Constructor, take in the specific model class and pass the db.model back to the parent'''
    def __init__(self, entityModel:db.Model):
        self.entitymodel = entityModel
    
    def read_by_id(self, id: int) -> db.Model:
        '''Service function to read a model from the database by id'''

        selected = self.entitymodel.query.filter(self.entitymodel.id == id).first()
        return selected