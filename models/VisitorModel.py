from sqlalchemy import Integer, String, Float, DateTime

from controllers import db

class Visitor(db.Model):
    __tablename__ = 'visitor'

    visitor_id = db.Column(Integer, primary_key=True, autoincrement = True)
    uuid = db.Column(String(60), nullable=False, unique=True)
    token_id = db.Column(String(60), nullable=False, unique=True)
    name = db.Column(String(60), nullable=False)
    email = db.Column(String(60), nullable=False)

    # One to many relationship with prediction
    predictions = db.relationship('models.PredictionModel.Prediction', back_populates='visitor')