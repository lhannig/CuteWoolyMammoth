import pytest
import db.connections as c

from sqlalchemy_utils.functions import database_exists

def test_create_or_connect():
    db_url = 'sqlite:///MammothDB.db'
    c.create_or_connect()


    assert database_exists(db_url)