import pytest 
import os
import pandas as pd
from datetime import datetime
from numpy import ndarray

from controllers import app as client
from controllers import db as database
from models import Data, QAModel

tester = client.app.test_client()

@pytest.fixture
def db():
    """
    Fixture to yield use of the database
    """

    yield database

@pytest.fixture
def app():
    """
    Fixture to yield use of the tester 
    """

    yield tester

def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """

    client.app.config['TESTING'] = True
    client.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    database.drop_all()
    database.create_all()
    database.session.commit()

    # Add a model 
    qa_model = QAModel(
        ml_type="BERT-BASE",
        ml_version="1.0",
        bleu_score=80.0,
        rouge_score=80.0,
        meteor_score=80.0,
        created_date=datetime.now()
    )
    
    database.session.add(qa_model)
    database.session.commit()

    # Load some sample datafor the wordcloud
    df = pd.read_json('https://raw.githubusercontent.com/sweng480-team23/tweet-qa-data/main/train.json')
    data: ndarray = df.values[1:100, :]
    
    for datum in data: 
        d = Data(
            question=datum[0],
            answer=datum[1],
            tweet=datum[2],
            qid=datum[3],
            created_date=datetime.now(),
            updated_date=datetime.now(),
            source='original dataset',
            start_position=1,
            end_position=1
        )
        database.session.add(d)
        database.session.commit()


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """

    database.session.close()
    os.remove('controllers/test.db')