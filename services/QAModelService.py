
from controllers import db
from models.AccountModel import Account
from models.DataModel import Data
from models.PredictionModel import Prediction
from models.QAModel import QAModel
import string

class QAModelService(object):
    db_conn = db
    def create_qa_model(self, model: QAModel) -> QAModel:
        self.db_conn.session.add(model)
        self.db_conn.session.commit()
        saved_model = self.read_qa_model_by_uuid(model.uuid)
        return saved_model

    def read_qa_model_by_uuid(self, model_uuid: string) -> QAModel:
        selected_model = QAModel.query.filter(QAModel.uuid == model_uuid).first()
        return selected_model

    def read_all_qa_model_by_type(self, model_type: string) -> list:
        selected_models = QAModel.query.filter(QAModel.ml_type == model_type).all()
        return selected_models

    def read_latest_qa_model_by_type(self, model_type: string) -> QAModel:
        selected_model = QAModel.query.filter(QAModel.ml_type == model_type).order_by(QAModel.created_date.desc()).first()
        return selected_model