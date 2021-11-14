from datetime import datetime
from sqlalchemy.sql.sqltypes import String
from controllers import db
from models.AccountModel import Account
from models.DataModel import Data
from models.PredictionModel import Prediction
from models.QAModel import QAModel


class DataService():
    db_conn = db

    def create_data(self, datum:Data)->Data:
        self.db_conn.session.add(datum)
        self.db_conn.session.commit()
        saved_data = self.read_data_by_qid(datum.qid)
        return saved_data

    def read_data_by_qid(self, qid:String)->Data:
        selected_data = Data.query.filter(Data.qid == qid).first()
        return selected_data

    def read_all_data_since(self, date:datetime)->list:
        selected_datas = Data.query.filter(Data.created_date > date).all()
        return selected_datas

    def read_last_x_datum(self, x:int)->list:
        selected_datas = Data.query.order_by(Data.datum_id.desc()).limit(x)
        selected_datas = selected_datas [::-1]
        return selected_datas

    def update_data (self, datum:Data)->Data:
        selected_data = Data.query.filter(Data.uuid == datum.uuid).first()
        selected_data.qid = datum.qid
        selected_data.tweet = datum.tweet
        selected_data.question = datum.question
        selected_data.answer = datum.answer
        selected_data.created_date = datum.created_date
        selected_data.updated_date = datum.updated_date
        selected_data.source = datum.source
        selected_data.answer = datum.answer
        selected_data.start_position = datum.start_position
        selected_data.end_position = datum.end_position
        self.db_conn.session.commit()
        saved_data = self.read_data_by_qid(datum.qid)
        return saved_data

    def generate_word_cloud(self, model:QAModel)->list:
        pass
        #not implemented at this moment
#End of DataService Class


