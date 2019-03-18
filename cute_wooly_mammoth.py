import os
from sqlalchemy import create_engine
from models import *



def setup_db():
    """create new db and add tables"""

    db_user = os.getenv("CWM_DB_USER")
    db_password = os.getenv("CWM_DB_PASSWORD")
    db_port = os.getenv("CWM_DB_PORT")
    db_name = os.getenv("CWM_DB_NAME")
    engine = create_engine("postgresql://{}:{}@localhost:{}/{}".format(db_user, db_password, db_port,
                                                                                       db_name), echo=True)
    Base.metadata.create_all(engine)


if __name__ == "__main__":


    setup_db()


