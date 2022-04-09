import connexion
import sys
from connexion.resolver import MethodViewResolver
from decouple import config
from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def configure_prod_db(_app: Flask) -> Flask:
    secret_key = config('SECRET_KEY')
    runner_address = config('RUNNER_ADDRESS')
    _app.app.config['SECRET_KEY'] = secret_key
    _app.app.config['RUNNER_ADDRESS'] = runner_address
    _app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false'
    _app.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:' + secret_key + '@ljdub.com:3306/mysql_database'
    return _app


def configure_dev_db(_app: Flask) -> Flask:
    _app.app.config['TESTING'] = True
    _app.app.config['RUNNER_ADDRESS'] = 'no-ip'
    _app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    _app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return _app


def configure_endpoints(_app: Flask) -> Flask:
    from containers import Container
    _app.container = Container()
    _app.add_api('../swagger.yml', pythonic_params=True)
    _app.add_api('../v2.yaml', resolver=MethodViewResolver('controllers.v2'))
    return _app

def create_app() -> Flask:
    _app = connexion.App(__name__, specification_dir='./')
    CORS(_app.app)
    if 'pytest' in sys.argv[0]:
        return configure_dev_db(_app)
    return configure_prod_db(_app)


app = create_app()
db = SQLAlchemy(app.app)
app = configure_endpoints(app)
