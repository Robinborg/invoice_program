if __name__ == "__main__" and __package__ is None:
    import sys
    from os import path
    var = path.dirname(path.abspath(__file__)) + "/../invoice"
    sys.path.append(var)

import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from models.product import Product
from models import Base

#Base.metadata.create_all(self.engine)
Session = sessionmaker()


def setup_module():
    global transaction, connection, engine
    engine = create_engine("sqlite:///invoices.db")
    connection = engine.connect()
    transaction = connection.begin()
    Base.metadata.create_all(connection)

def teardown_module():
    transaction.rollback()
    connection.close()
    engine.dispose()

class TestConnection(unittest.TestCase):

    def setup(self):
        self.__transaction = connection.begin_nested()
        self.session = Session(connection)

    def teardown(self):
        self.session.close()
        self.__transaction.rollback()

if __name__ == "__main__":
    unittest.main()
