from sqlalchemy import String, Integer

from controllers import db

class Account(db.Model):
    __tablename__ = 'account'

    account_id = db.Column(Integer, primary_key=True, autoincrement = True)
    username = db.Column(String(60), nullable=False)
    #TODO: convert password plain text to hash/salt password 
    password = db.Column(String(60), nullable=False)
    email = db.Column(String(60), nullable=False)

    # tostring code use for testing and debug
    def __repr__(self)->str:
        return (f'Username: {self.username}, \n' +
                f'Email: {self.email}, \n')