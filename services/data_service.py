from datetime import datetime
from services.create_read_update_service import CreateReadUpdateService
from services.qa_model_service import QAModelService
from controllers import db
from models import Data, QAModel
from typing import List
from tqatypes.word_response import WordResponse
import pandas as pd
import string


class DataService(CreateReadUpdateService):
    """ DataService, functions inherited from CreateReadUpdateService : read_by_id(id), create(entity_model), update(entity_model) """

    def __init__(self):
        '''Constructor, take in the specific model class and pass the db.model back to the parent'''
        super().__init__(Data)
        self.model_service: QAModelService = QAModelService()

    """ functions inherited from CreateReadUpdateService : read_by_id(id), create(entity_model), update(entity_model) """


    def read_all_data_since(self, date: datetime) -> List[Data]:
        selected_datas = Data.query.filter(Data.created_date > date).all()
        return selected_datas

    def read_last_x_datum(self, x: int) -> List[Data]:
        selected_datas = Data.query.order_by(Data.id.desc()).limit(x)
        selected_datas = selected_datas[::-1]
        return selected_datas

    def generate_word_cloud(self, model_id: int) -> List[WordResponse]:
        model: QAModel = self.model_service.read_by_id(model_id)
        data: List[Data] = self.read_all_data_since(model.created_date)
        word_list: List[str] = []
        [[word_list.append(word)
            for word in datum.tweet.translate(str.maketrans('', '', string.punctuation)).lower().split()]
            for datum in data]
        word_counts: List = pd.Series(word_list).value_counts().to_dict()
        return [{'name': key, 'weight': value} for key, value in word_counts.items()]
