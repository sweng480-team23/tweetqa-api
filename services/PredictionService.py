from datetime import datetime
from sqlalchemy.sql.sqltypes import String
from controllers import db
from models.AccountModel import Account
from models.DataModel import Data
from models.PredictionModel import Prediction
from models.QAModel import QAModel
from models.VisitorModel import Visitor
from services.DataService import DataService
from services.QAModelService import QAModelService
import string


class PredictionService():
    db_conn = db
    data_service = DataService()
    model_service = QAModelService()

    def create_prediction(self, prediction:Prediction)->Prediction:
        self.db_conn.session.add(prediction)
        self.db_conn.session.commit()
        saved_prediction = Prediction.query.filter(Prediction.uuid == prediction.uuid).first()
        return saved_prediction

    def update_prediction(self, prediction:Prediction)->Prediction:
        prediction_retrieve = Prediction.query.filter(Prediction.uuid == prediction.uuid).first()
        prediction_retrieve.prediction = prediction.prediction
        prediction_retrieve.alt_answer = prediction.alt_answer
        prediction_retrieve.is_corrected = prediction.is_corrected
        prediction_retrieve.visitor_id = prediction.visitor_id
        prediction_retrieve.model_id = prediction.model_id
        prediction_retrieve.datum_id = prediction.datum_id
        self.db_conn.session.commit()
        saved_prediction = Prediction.query.filter(Prediction.uuid == prediction.uuid).first()
        return saved_prediction

    def get_prediction(self, uuid:string)->Prediction:
        prediction_retrieve = Prediction.query.filter(Prediction.uuid == uuid).first()
        return prediction_retrieve
