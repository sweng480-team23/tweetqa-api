from datetime import datetime, timedelta
import pytest 
import os
from flask_sqlalchemy import SQLAlchemy

from controllers import app as client
from controllers import db as database

from services import DataService
from services import QAModelService

from dtos import DataCreateRequestV2
from dtos import QAModelCreateRequestV2
from models import Data
from models import QAModel
from tests.mock.dtos.v2 import MockDataCreateRequestV2
from tests.mock.dtos.v2 import MockQAModelCreateRequestV2

tester = client.app.test_client()

@pytest.fixture
def db():
    """
    Fixture to provide use of the test database
    """
    yield database

@pytest.fixture
def app():
    """
    Fixture to provide use of the test client
    """
    yield tester

@pytest.fixture
def data_model(db: SQLAlchemy):
    """
    Fixture to provide use and clean up of data model class
    """
    dto: DataCreateRequestV2 = MockDataCreateRequestV2()
    data: Data = dto.to_model()
    
    yield data

    db.session.delete(data)
    db.session.commit()

@pytest.fixture
def data_service():
    """
    Fixture to provide use of data service class
    """
    service = DataService()
    yield service

@pytest.fixture
def qa_model_model(db: SQLAlchemy):
    dto: QAModelCreateRequestV2 = MockQAModelCreateRequestV2()
    qa_model = dto.to_model()

    yield qa_model
    
    db.session.delete(qa_model)
    db.session.commit()

@pytest.fixture
def qa_model_service():
    """
    Fixture to provide use of the qa model service class
    """
    service = QAModelService()
    yield service


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """

    client.app.config['TESTING'] = True
    client.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    database.drop_all()
    database.create_all()



def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """

    database.session.close()
    os.remove('controllers/test.db')