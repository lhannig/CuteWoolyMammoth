import pytest
import sqlalchemy
from sqlalchemy import create_engine
from app.database import connections
from app.database import models


from sqlalchemy_utils.functions import database_exists

db_url = 'sqlite:///MammothDB.db'


def test_create_or_connect():

    session = connections.create_or_connect()


    assert database_exists(db_url) == True


def test_initialdata():

    session = connections.make_session()
    query = session.query(models.Wash).all()

    assert len(query) == 3
