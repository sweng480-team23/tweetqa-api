from sqlalchemy import String, Integer

from controllers import db

class AccountModel(db.Model):
    __tablename__ = 'account'

    account_id = db.Column(Integer, primary_key=True)
    uuid = db.Column(String(60), nullable=False, unique=True)
    password = db.Column(String(60), nullable=False)
    email = db.Column(String(60), nullable=False)