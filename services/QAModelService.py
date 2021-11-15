
from controllers import db
from dtos.v1.QAModelDTOs import QAModelResponse
from models import QAModel
import string

class QAModelService(object):
    '''Service class to handle all database CRUD operations for models'''

    
    def create_qa_model(self, model: QAModel) -> QAModel:
        '''Service function to create a new model in the database'''

        db.session.add(model)
        db.session.commit()

        saved_model = self.read_qa_model_by_id(model.id)
        return saved_model

    def read_qa_model_by_id(self, id: string) -> QAModel:
        '''Service function to read a model from the database by id'''

        selected_model = QAModel.query.filter(QAModel.id == id).first()
        return selected_model

    def read_all_qa_model_by_type(self, model_type: string) -> list:
        '''Service function to read all models by a given type'''

        selected_models = QAModel.query.filter(QAModel.ml_type == model_type).all()
        return selected_models

    def read_latest_qa_model_by_type(self, model_type: string) -> QAModel:
        '''Service function to read the latest model by type'''

        selected_model = QAModel.query.filter(QAModel.ml_type == model_type).order_by(QAModel.created_date.desc()).first()
        return selected_model

    def read_latest_models(self) -> list:
        '''Service function used to retrive the latest models for each type'''

        #TODO: Not working correctly
        models = QAModel.query.order_by(QAModel.created_date.desc()).distinct(QAModel.ml_type)
        return models

