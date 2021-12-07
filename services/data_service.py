from datetime import datetime

from controllers import db
from models import Data, QAModel


class DataService():

    def create_data(self, datum:Data) -> Data:
        db.session.add(datum)
        db.session.commit()
        saved_data = self.read_data_by_id(datum.id)
        return saved_data

    def read_data_by_id(self, id: str) -> Data:
        selected_data = Data.query.filter(Data.id == id).first()
        return selected_data

    def read_all_data_since(self, date: datetime) -> list:
        selected_datas = Data.query.filter(Data.created_date > date).all()
        return selected_datas

    def read_last_x_datum(self, x: int) -> list:
        selected_datas = Data.query.order_by(Data.id.desc()).limit(x)
        selected_datas = selected_datas [::-1]
        return selected_datas

    def update_data (self, datum: Data) -> Data:
        selected_data = Data.query.filter(Data.id == datum.id).first()
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
        db.session.commit()
        saved_data = self.read_data_by_id(datum.id)
        return saved_data

    def generate_word_cloud(self, model:QAModel)->list:

        raise NotImplementedError


