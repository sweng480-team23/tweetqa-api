from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import String
from controllers import db
from models.AccountModel import Account
from models.DataModel import Data
from models.PredictionModel import Prediction
from models.QAModel import QAModel
from sqlalchemy.orm import sessionmaker
import string

class AccountService():
    db_conn = db

    def create_account(self, account:Account)->Account:
        self.db_conn.session.add(account)
        self.db_conn.session.commit()
        saved_account = self.login(account.username,account.password)
        return saved_account

    #Testing class
    """
    def read_account(self, name:string)->Account:
        selected_data = Account.query.filter_by(username=name).first()
        if  selected_data is None:
            print('No item returned')
        return selected_data
    """
    #login function 
    #check if the username and password combination exist in the database
    #if not, return null object
    def login(self, username:string, password:string)->Account:
        login_user = Account.query.filter_by(username=username).first()
        if login_user is None:
            return null
        elif login_user.password == password:
            return login_user
        return null

    def generate_token_invitation_for_email(self, email:string):
        pass
        #to be implemented

#End of AccountService Class
