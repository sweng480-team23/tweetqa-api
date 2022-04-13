from sqlalchemy import String, DateTime, Integer, Boolean
from controllers import db
from models import IdentifiableEntity


class Training(IdentifiableEntity):
    __tablename__ = 'training'

    created = db.Column(DateTime, nullable=False)
    epochs = db.Column(Integer, nullable=False)
    learningRate = db.Column(String(10), nullable=False)
    batchSize = db.Column(Integer, nullable=False)
    baseModel = db.Column(String(100), nullable=False)
    lastXLabels = db.Column(Integer, nullable=False)
    includeUserLabels = db.Column(Boolean, nullable=False)
    admin_id = db.Column(Integer, db.ForeignKey('account.id'), nullable=False)
    admin = db.relationship('models.account_model.Account', back_populates='trainings')

    def __repr__(self) -> str:
        return f"""
            Training Id: {self.id}, 
            Created: {self.created}, 
            Base Model: {self.baseModel},
            Epochs: {self.epochs},
            Learning Rate: {self.learningRate},
            Batch Size: {self.batchSize}"""
