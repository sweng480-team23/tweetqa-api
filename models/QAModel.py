from sqlalchemy import Integer, String, Float, DateTime

from controllers import db

class QAModel(db.Model):
    __tablename__ = 'qa_model'

    model_id = db.Column(Integer, primary_key=True)
    uuid = db.Column(Integer, nullable=False, unique=True)

    ml_type = db.Column(String(100), nullable=False)
    ml_version = db.Column(String(20), nullable=False)

    bleu_score = db.Column(Float, nullable=False)
    rogue_score = db.Column(Float, nullable=False)
    meteor_score = db.Column(Float, nullable=False)

    created = db.Column(DateTime, nullable=False)

    # One to many relationship with prediction
    predictions = db.relationship('models.PredictionModel.PredictionModel', back_populates='model')

    def __repr__(self) -> str:
        return (f'Model id: {self.model_id}, Model: {self.ml_type}-{self.ml_version}, ' +
                f'Scores: [{self.bleu_score}, {self.rogue_score}, {self.meteor_score}], ' +
                f'Created: {self.created}')