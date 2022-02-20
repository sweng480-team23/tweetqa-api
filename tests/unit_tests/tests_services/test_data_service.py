from multiprocessing.context import assert_spawning
import pytest
from datetime import datetime
from flask.testing import FlaskClient
from services.data_service import DataService
from models import Data


def test_root(app: FlaskClient):
    """
    Smoke test to ensure the application isnt on fire
    """
    response = app.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b'"The TweetQA Api is running!"\n'

@pytest.fixture
def data_model(db):
    data = Data(
        qid='test qid',
        tweet='test tweet',
        question='test question',
        answer='test answer',
        created_date=datetime.now(),
        updated_date=datetime.now(),
        source='original dataset',
        start_position=1,
        end_position=1
    )

    yield data

    db.session.delete(data)
    db.session.commit()

@pytest.fixture
def data_service():
    service = DataService()

    yield service

@pytest.mark.data
def test_data_service_creates_data(data_model: Data, data_service: DataService):
    """
    TC-001: The DataService object can create a datum entity in the database
    """

    data_out = data_service.create(data_model)
    data_saved = Data.query.filter(Data.id == data_model.id).first()
    
    assert data_saved is not None
    assert data_out is not None
    assert data_saved == data_out
    assert data_out == data_model

@pytest.mark.data
def test_data_service_reads_data_by_id(data_model: Data, data_service: DataService):
    """
    TC-002: The DataService object can read a datum entity from the database by id
    """

    data_service.create(data_model)
    data_out = data_service.read_by_id(data_model.id)

    assert data_out is not None
    assert data_out == data_model

@pytest.mark.data
def test_data_service_updates_data(data_model: Data, data_service: DataService):
    """
    TC-003: The DataService object can update an existing datum entity in the database
    """

    data_service.create(data_model)

    data_model.qid = 'updated qid'
    data_out = data_service.update(data_model)

    assert data_out is not None
    assert data_out == data_model

