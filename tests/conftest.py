import pytest
import os
from flask_sqlalchemy import SQLAlchemy
from typing import List

from controllers import app as client
from controllers import db as database

from models import *
from services import *
from dtos import *

from services.visitor_service import VisitorService
from tests.mock.dtos.v2 import MockDataCreateRequestV2
from tests.mock.dtos.v2 import MockQAModelCreateRequestV2
from tests.mock.dtos.v2.mock_visitor_dto_v2 import MockVisitorCreateRequestV2

tester = client.app.test_client()


@pytest.fixture
def db():
    yield database


@pytest.fixture
def app():
    yield tester


@pytest.fixture
def data_model(db: SQLAlchemy):
    dto: DataCreateRequestV2 = MockDataCreateRequestV2()
    data: Data = dto.to_model()

    yield data

    db.session.delete(data)
    db.session.commit()


@pytest.fixture
def data_model_list(db: SQLAlchemy):
    data_list: List[Data] = [MockDataCreateRequestV2().to_model()
                             for _ in range(10)]

    yield data_list

    for data in data_list:
        db.session.delete(data)
        db.session.commit()


@pytest.fixture
def data_service():
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
def qa_model_model_list(db: SQLAlchemy):
    qa_model_model_list: List[QAModel] = [
        MockQAModelCreateRequestV2().to_model() for _ in range(10)]

    yield qa_model_model_list

    for qa_model in qa_model_model_list:
        db.session.delete(qa_model)
        db.session.commit()


@pytest.fixture
def qa_model_service():
    service = QAModelService()
    yield service


@pytest.fixture
def visitor_model(db: SQLAlchemy):
    dto: VisitorCreateRequestV2 = MockVisitorCreateRequestV2()
    visitor_model = dto.to_model()

    yield visitor_model

    db.session.delete(visitor_model)
    db.session.commit()


@pytest.fixture
def visitor_service():
    service = VisitorService()
    return service


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
