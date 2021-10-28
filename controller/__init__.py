import connexion
from flask_sqlalchemy import SQLAlchemy 


app = connexion.App(__name__, specification_dir='./')

#app.app.config['SECRET_KEY'] = '653d72d9f6ed01acf0d4'
#app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false'
#app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#db = SQLAlchemy(app)

app.add_api('../swagger.yml')

from controller.v1 import routes
