from sqlalchemy import Integer, String, Float, DateTime

from controllers import db

class Visitor(db.Model):
    __tablename__ = 'visitor'

    id = db.Column(Integer, primary_key=True, autoincrement = True)
    token = db.Column(String(60), nullable=False, unique=True)
    name = db.Column(String(60), nullable=False)
    email = db.Column(String(60), nullable=False)

    # One to many relationship with prediction
    predictions = db.relationship('models.prediction_model.Prediction', back_populates='visitor')