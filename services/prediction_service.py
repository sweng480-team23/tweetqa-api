from controllers import db
from utils import first_runner
from models import Prediction


class PredictionService():

    def create_prediction(self, prediction:Prediction)->Prediction:
        prediction.prediction = first_runner.answer_tweet_question(prediction.datum.tweet, prediction.datum.question)
        db.session.add(prediction)
        db.session.commit()
        saved_prediction = Prediction.query.filter(Prediction.id == prediction.id).first()
        return saved_prediction

    def update_prediction(self, prediction: Prediction) -> Prediction:
        prediction_retrieve = Prediction.query.filter(Prediction.id == prediction.id).first()
        prediction_retrieve.alt_answer = prediction.alt_answer
        prediction_retrieve.is_correct = prediction.is_correct
        db.session.commit()
        saved_prediction = Prediction.query.filter(Prediction.id == prediction.id).first()
        return saved_prediction

    def read_prediciton_by_id(self, id: int) -> Prediction:
        prediction_retrieve = Prediction.query.filter(Prediction.id == id).first()
        return prediction_retrieve
