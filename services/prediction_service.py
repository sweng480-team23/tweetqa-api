from models import Prediction
from controllers import app
from .abstract.create_read_update_service import CreateReadUpdateService
import sys
import requests


class PredictionService(CreateReadUpdateService):
    ''' DataService, functions inherited from CreateReadUpdateService :
            read_by_id(id), create(entity_model), update(entity_model) '''

    def __init__(self):
        '''Constructor, take in the specific model class and pass the db.model back to the parent'''
        super().__init__(Prediction)

    def create(self, prediction: Prediction) -> Prediction:
        # todo: find a more elegant solution for mocking out the post request to runner service
        if 'pytest' not in sys.argv[0]:
            prediction.prediction = self.get_answer(prediction)
        else:
            prediction.prediction = "mock prediction"
        saved_prediction = super().create(prediction)
        return saved_prediction


    def get_answer(self, prediction: Prediction):
        runner_address = app.app.config['RUNNER_ADDRESS']
        dict_out = {"tweet": prediction.datum.tweet, "question": prediction.datum.question}
        res = requests.post(runner_address, json=dict_out)
        dict_in = res.json()
        return dict_in["answer"]


    def update(self, prediction: Prediction) -> Prediction:
        # TODO: Logic to be added to update the DATA collection
        saved_prediction = super().update(prediction)
        return saved_prediction
