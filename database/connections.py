# script for setting up the db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils.functions import database_exists
import logging
from app import Session
from .models import Base, Wash

db_url = 'sqlite:///MammothDB.db'
engine = create_engine(db_url)



logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def check_database_exists():
    """check if db exists"""

    if database_exists(db_url):
        return True
    else:
        return False

def create_db(session):
    """check if db exists, if not create new"""

    setup()
    insert_initial_data(session)

    return session


def setup():
    """create a new database"""

    my_metadata = Base.metadata
    my_metadata.create_all(engine)

    from alembic.config import Config
    from alembic import command
    alembic_cfg = Config('alembic.ini')
    command.stamp(alembic_cfg, 'head')





def make_session():
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

