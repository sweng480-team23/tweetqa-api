import connexion
import os
from decouple import config

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



app = connexion.App(__name__, specification_dir='./')
SECRET_KEY = os.getENV('SECRET_KEY')

CORS(app.app)
# App Config
app.app.config['SECRET_KEY'] = SECRET_KEY


app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false'
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:' + SECRET_KEY + '@ljdub.com:3306/mysql_database'
db = SQLAlchemy(app.app)

app.add_api('../swagger.yml', pythonic_params=True)
