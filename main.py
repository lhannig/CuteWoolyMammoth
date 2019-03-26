import os

from database import connections

if __name__ == "__main__":



    db_exists = connections.database_exists(connections.db_url)

    if db_exists == False:
        session = connections.make_session()
        connections.create_db(session)

    else:
        session = connections.make_session()



