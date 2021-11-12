from controllers import db
from models.AccountModel import Account
from models.DataModel import Data
from models.PredictionModel import Prediction
from models.QAModel import QAModel

class DataService():
    db_conn = db
    @classmethod
    def create_data(self, datum:Data):
        db.session.add(datum)
        db.session.commit()
#End of DataService Class


