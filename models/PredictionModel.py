from sqlalchemy import Integer, String, Boolean

from controllers import db


class PredictionModel(db.Model):
    __tablename__ = 'model'

    response_id = db.Column(Integer, primary_key=True)
    uuid = db.Column(String(60), nullable=False, unique=True)
    token_id = db.Column(String(60), nullable=False)
    is_corrected = db.Column(Boolean, nullable=False)
    alt_answer = db.Column(String(280), nullable=True)

    # many to one relatioonship with Model
    model_id = db.Column(Integer, db.ForeignKey('qa_model.model_id'), nullable=False)
    model = db.relationship('models.QAModel.QAModel', back_populates='predictions')

    # many to one relationship with Data
    datum_id = db.Column(Integer, db.ForeignKey('data.datum_id'), nullable=False)
    data = db.relationship('models.DataModel.DataModel', back_populates='predictions')

    def __repr__(self) -> str:
        return f'Prediction {self.response_id}'