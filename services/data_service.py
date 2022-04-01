from datetime import datetime
from itertools import count
from services.abstract.create_read_update_service import CreateReadUpdateService
from services.qa_model_service import QAModelService
from sqlalchemy.sql import func
from models.data_model import Data
from models.qa_model import QAModel
from typing import List
from typing import Dict
from tqatypes.word_response import WordResponse
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords', quiet=True)
import pandas as pd
import random
import string
import timeit


class DataService(CreateReadUpdateService):
    """ DataService, functions inherited from CreateReadUpdateService : read_by_id(id), create(entity_model), update(entity_model) """


    def __init__(self):
        '''Constructor, take in the specific model class and pass the db.model back to the parent'''
        super().__init__(Data)
        self.model_service: QAModelService = QAModelService()
        self.stop_words = set(stopwords.words('english'))

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
            for word in datum.tweet.translate(str.maketrans('', '', string.punctuation)).lower().split()
            if not word in self.stop_words]
            for datum in data]
        word_counts: Dict = pd.Series(word_list, dtype=str).value_counts().head(100).to_dict()
        return [{'name': key, 'weight': value} for key, value in word_counts.items()]

    def read_random(self)->Data:
        # id_list: List[int] = []
        # all_datas = Data.query.all()
        # for datum in all_datas:
        #     id_list.append(datum.id)
        # #print(id_list)
        # random_id = random.choice(id_list)
        # #print(random_id)
        # random_data = self.read_by_id(random_id)
        # #print(random_data)
        starttime = timeit.default_timer()
        random_data = Data.query.order_by(func.random()).first()
        #print(random_data)
        print(timeit.default_timer()-starttime)
        return random_data

