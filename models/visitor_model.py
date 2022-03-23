from sqlalchemy import Integer, String
from controllers import db
from models import IdentifiableEntity

print(f'Visitor Model: {db.engine.url}')
class Visitor(IdentifiableEntity):
    __tablename__ = 'visitor'

    token = db.Column(String(60), nullable=False, unique=True)
    email = db.Column(String(60), nullable=False)

    # One to many relationship with prediction
    predictions = db.relationship('models.prediction_model.Prediction', back_populates='visitor')

    # many to one relationship with admin account
    # For declaring foreign key : db.Foreignkey('tablename.columnname')
    # For specifying the relationship, db.relationship('packagename.filename.classname', back_populates = 'columnname specified in the class')
    invitor_account = db.Column(Integer, db.ForeignKey('account.id'), nullable=False)
    invitor = db.relationship('models.account_model.Account', back_populates='visitor')

    # tostring code use for testing and debug
    def __repr__(self) -> str:
        return (f'Visitor id: {self.id}, '+ f'Token:{self.token} '+ f'Email:{self.email}')
