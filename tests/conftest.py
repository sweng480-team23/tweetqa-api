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
    df = pd.read_json('https://raw.githubusercontent.com/sweng480-team23/tweet-qa-data/main/dev.json')
    df = df.head(100)

    for _, row in df.iterrows():
        row["Answer"] = row["Answer"][0]

    for _, row in df.iterrows(): 

        try:
            d = Data(
                question=row["Question"],
                answer=row["Answer"],
                tweet=row["Tweet"],
                qid=row["qid"],
                created_date=datetime.now(),
                updated_date=datetime.now(),
                source='dev dataset',
                start_position=1,
                end_position=5
            )
            database.session.add(d)
            database.session.commit()
        except:
            continue


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """

    database.session.close()
    os.remove('controllers/test.db')