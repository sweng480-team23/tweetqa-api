from sqlalchemy import Integer, String, DateTime
from controllers import db
from models import IdentifiableEntity


class Data(IdentifiableEntity):
    __tablename__ = 'data'

    qid = db.Column(String(35), nullable=True, unique=True)

    tweet = db.Column(String(400), nullable=False)
    question = db.Column(String(280), nullable=False)
    answer = db.Column(String(280), nullable=True)

    created_date = db.Column(DateTime, nullable=False)
    updated_date = db.Column(DateTime, nullable=False)

    source = db.Column(String(35), nullable=False)

    start_position = db.Column(Integer)
    end_position = db.Column(Integer)

    # For specifying the relationship, db.relationship('packagename.filename.classname', back_populates = 'columnname specified in the class')
    predictions = db.relationship('models.prediction_model.Prediction', back_populates='datum')

    def __repr__(self):
        return (f'Id: {self.id}, \n' +
                f'Tweet: {self.tweet}, \n' +
                f'Question: {self.question}, \n' +
                f'Answer: {self.answer}')
