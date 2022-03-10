from typing import List
from controllers import db
from models import QAModel
from .abstract.create_read_update_service import CreateReadUpdateService

class QAModelService(CreateReadUpdateService):
    ''' Service class to handle all database CRUD operations for models,
        functions inherited from CreateReadUpdateService : read_by_id(id), create(entity_model), update(entity_model)'''

    def __init__(self):
        '''Constructor, take in the specific model class and pass the db.model back to the parent'''
        super().__init__(QAModel)

    def read_all_qa_model_by_type(self, model_type: str) -> List[QAModel]:
        '''Service function to read all models by a given type'''

        selected_models = QAModel.query.filter(QAModel.ml_type == model_type).all()
        return selected_models

    def read_latest_qa_model_by_type(self, model_type: str) -> QAModel:
        '''Service function to read the latest model by type'''

        selected_model = QAModel.query.filter(QAModel.ml_type == model_type).\
            order_by(QAModel.created_date.desc()).first()
        return selected_model

    def read_latest_models(self) -> List[QAModel]:
        '''Service function used to retrive the latest models for each type'''
        # First get the list of unique model name from the query
        selected_models_name = db.session.query(QAModel.ml_type).distinct().all()
        # create an empty list
        selected_models = []
        # For each of the unique model name, query the database to return the latest one and apend to the list
        for name in selected_models_name:
            selected_model = QAModel.query.filter(QAModel.ml_type == name[0]).order_by(QAModel.created_date.desc()).first()
            selected_models.append(selected_model)
        return selected_models

