from datetime import datetime
from typing import List
from flask_sqlalchemy import SQLAlchemy
from models.DataModel import DataModel

class DataService:
    def __init__(self, db: SQLAlchemy) -> None:
        self.db = db

    def create_data(self, datum: DataModel) -> DataModel:
        # todo
        pass

    def read_data_by_qid(self, qid: str) -> DataModel:
        # todo
        pass

    def read_all_data_since(self, date: datetime) -> List[DataModel]:
        # todo
        pass

    def read_last_x_datum(self, x: int) -> List[DataModel]:
        # todo
        pass

    def update_data(self, datum: DataModel) -> DataModel:
        # todo
        pass