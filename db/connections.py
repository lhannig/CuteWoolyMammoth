# script for setting up the db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils.functions import database_exists
import logging
from db import Session
from .models import Base, Wash

db_url = 'sqlite:///MammothDB.db'



logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def create_or_connect():
    """check if db exists, if not create new"""

    engine = create_engine(db_url)

    if database_exists(db_url):
        session = make_session(engine)

    else:
        setup(engine)
        session = make_session(engine)
        insert_initial_data(session)




def setup(engine):
    """create a new database"""

    my_metadata = Base.metadata
    my_metadata.create_all(engine)

    from alembic.config import Config
    from alembic import command
    alembic_cfg = Config('alembic.ini')
    command.stamp(alembic_cfg, 'head')


def make_session(engine):
    """establishes a connection to the db"""

    Session.configure(bind=engine)
    session = Session()

    return session

def insert_initial_data(session):
    """insert initial data for needlesize, wash, and weight"""

    handwash = Wash(name='Handwash')
    session.add(handwash)

    coolwash = Wash(name='Machine wash cool, gentle cycle')
    session.add(coolwash)

    warmwash = Wash(name='Machine wash warm, gentle cycle')
    session.add(warmwash)
    session.commit()

