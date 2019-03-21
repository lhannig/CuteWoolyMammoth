import os

from db import connections

if __name__ == "__main__":

    session = connections.create_or_connect()


