from sqlalchemy import Integer, String, DateTime, Boolean

from controllers import db

class DataModel(db.Model):
    __tablename__ = 'data'

    datum_id = db.Column(Integer, primary_key=True)
    qid = db.Column(String(32), nullable=False, unique=True)

    tweet = db.Column(String(280), nullable=False)
    question = db.Column(String(280), nullable=False)
    answer = db.Column(String(280), nullable=False)

    created = db.Column(DateTime, nullable=False)
    updated = db.Column(DateTime, nullable=False)

    original = db.Column(Boolean, nullable=False)

    start_position = db.Column(Integer)
    end_position = db.Column(Integer)

    predictions = db.relationship('models.PredictionModel.PredictionModel', back_populates='data')

    def __repr__(self):
        return (f'Id: {self.datum_id}, \n' +
                f'Tweet: {self.tweet}, \n' +
                f'Question: {self.question}, \n' +
                f'Answer: {self.answer}')