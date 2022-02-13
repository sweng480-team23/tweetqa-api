from venv import create
from controllers import db
from models.qa_model import QAModel
from utils import first_runner
from models import Prediction
from services.create_read_update_service import CreateReadUpdateService


class PredictionService(CreateReadUpdateService):
    ''' DataService, functions inherited from CreateReadUpdateService :
            read_by_id(id), create(entity_model), update(entity_model) '''

    def __init__(self):
        '''Constructor, take in the specific model class and pass the db.model back to the parent'''
        super().__init__(Prediction)

    # Wrapper function to create
    def create_prediction(self, prediction:Prediction)->Prediction:
        model_prediction = first_runner.answer_tweet_question(prediction.datum.tweet, prediction.datum.question)
        prediction.prediction = model_prediction[0]

        saved_prediction = self.create(prediction)
        return saved_prediction

    # Wrapper function to update
    def update_prediction(self, prediction: Prediction) -> Prediction:
        # TODO: Logic to be added to update the DATA collection
        saved_prediction = self.update(prediction)
        return saved_prediction

