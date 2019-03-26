import pytest
import sqlalchemy
from sqlalchemy import create_engine
from app.database import connections
from app.database import models

session = connections.make_session()
connections.create_db(session)



def test_initialdata():


    query = session.query(models.Wash).all()

    assert len(query) == 3
