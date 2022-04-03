from sqlalchemy import String
from controllers import db
from .abstract.identifiable_entity_model import IdentifiableEntity


class Account(IdentifiableEntity):
    __tablename__ = 'account'

    #TODO: convert password plain text to hash/salt password 
    password = db.Column(String(60), nullable=False)
    email = db.Column(String(60), nullable=False)

    # One to many relationship with visitor
    visitor = db.relationship('models.visitor_model.Visitor', back_populates='invitor')
    trainings = db.relationship('models.training_model.Training', back_populates='admin')

    # tostring code use for testing and debug
    def __repr__(self)->str:
        return (f'Password: {self.password}, \n' +
                f'Email: {self.email}, \n')