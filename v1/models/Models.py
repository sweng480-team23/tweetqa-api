from sqlalchemy import Integer, String, Float, DateTime, Boolean
from v1 import db

class QAModel(db.Model):
    __tablename__ = 'qa_model'

    __model_id = db.Column(Integer, primary_key=True)
    __uuid = db.Column(Integer, nullable=False, unique=True)

    __ml_type = db.Column(String(100), nullable=False)
    __ml_version = db.Column(String(20), nullable=False)

    __bleu_score = db.Column(Float, nullable=False)
    __rogue_score = db.Column(Float, nullable=False)
    __meteor_score = db.Column(Float, nullable=False)

    __created = db.Column(DateTime, nullable=False)

    # One to many relationship with prediction
    __predictions = db.relationship('Prediction', back_populates='model')

    def __repr__(self) -> str:
        return (f'Model id: {self.__model_id}, Model: {self.__ml_type}-{self.__ml_version}, ' +
                f'Scores: {self.__bleu_score}, {self.__rogue_score}, {self.__meteor_score}' +
                f'Created: {self.__created}')


class Data(db.Model):
    __tablename__ = 'data'

    __datum_id = db.Column(Integer, primary_key=True)
    __qid = db.Column(String(32), nullable=False, unique=True)

    __tweet = db.Column(String(280), nullable=False)
    __question = db.Column(String(280), nullable=False)
    __answer = db.Column(String(280), nullable=False)

    __created = db.Column(DateTime, nullable=False)
    __updated = db.Column(DateTime, nullable=False)

    __original = db.Column(Boolean, nullable=False)

    __start_position = db.Column(Integer)
    __end_position = db.Column(Integer)

    __predictions = db.relationship('Prediction', back_populates='__data')

    def __repr__(self):
        return (f'Id: {self.__datum_id}, ' +
                f'Tweet: {self.__tweet}' +
                f'Question: {self.__question}' +
                f'Answer: {self.__answer}')

class Prediciton(db.Model):
    __tablename__ = 'model'

    __response_id = db.Column(Integer, primary_key=True)
    __uuid = db.Column(Integer, unique=True)
    __token_id = db.Column(String(60), nullable=False)
    __is_corrected = db.Column(Boolean, nullable=False)
    __alt_answer = db.Column(String(280), nullable=True)

    # many to one relatioonship with Model
    __model_id = db.Column(Integer, db.ForeignKey('qa_model.__model_id'), nullable=False)
    __model = db.relationship('QAModel', back_populates='__predictions')

    # many to one relationship with Data
    __datum_id = db.Column(Integer, db.ForeignKey('data.__datum_id'), nullable=False)
    __data = db.relationship('Data', back_populates='__predictions')