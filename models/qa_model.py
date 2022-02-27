from sqlalchemy import String, Float, DateTime
from controllers import db
from models import IdentifiableEntity


class QAModel(IdentifiableEntity):
    __tablename__ = 'qa_model'

    ml_type = db.Column(String(100), nullable=False)
    ml_version = db.Column(String(20), nullable=False)
    bleu_score = db.Column(Float, nullable=False)
    rouge_score = db.Column(Float, nullable=False)
    meteor_score = db.Column(Float, nullable=False)
    created_date = db.Column(DateTime, nullable=False)
    model_url = db.Column(String(200), nullable=True)
    # One to many relationship with prediction
    predictions = db.relationship('models.prediction_model.Prediction', back_populates='model')

    # tostring code use for testing and debug
    def __repr__(self) -> str:
        return (f'Model id: {self.id}, Model: {self.ml_type}-{self.ml_version}, ' +
                f'Scores: [{self.bleu_score}, {self.rouge_score}, {self.meteor_score}], ' +
                f'Created: {self.created_date}.' + f'Url:{self.model_url}')
