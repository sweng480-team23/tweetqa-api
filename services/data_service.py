from datetime import datetime
from services.create_read_update_service import CreateReadUpdateService
from controllers import db
from models import Data, QAModel


class DataService(CreateReadUpdateService):
    """ DataService, functions inherited from CreateReadUpdateService : read_by_id(id), create(entity_model), update(entity_model) """

    def __init__(self):
        '''Constructor, take in the specific model class and pass the db.model back to the parent'''
        super().__init__(Data)

    """ functions inherited from CreateReadUpdateService : read_by_id(id), create(entity_model), update(entity_model) """


    def read_all_data_since(self, date: datetime) -> list:
        selected_datas = Data.query.filter(Data.created_date > date).all()
        return selected_datas

    def read_last_x_datum(self, x: int) -> list:
        selected_datas = Data.query.order_by(Data.id.desc()).limit(x)
        selected_datas = selected_datas [::-1]
        return selected_datas

    def generate_word_cloud(self, model:QAModel)->list:

        raise NotImplementedError


