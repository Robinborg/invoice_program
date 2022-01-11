if __name__ == "__main__" and __package__ is None:
    import sys
    from os import path
    var = path.dirname(path.abspath(__file__)) + "/../src"
    sys.path.append(var)

import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from models.customer import Customer
from models import Base

class TestQuery(unittest.TestCase):

    engine = create_engine("sqlite:///invoices.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    
    def setUp(self):
        Base.metadata.create_all(self.engine)
        self.customer = Customer(name = "Joe",
                               address ="Main street",
                               phone = "555555")
        self.session.add(self.customer)
        self.session.commit()

    def teardown(self):
        Base.metadata.drop_all(self.engine)


    def test_query_product(self):
        expected = [self.customer]
        result = self.session.query(Customer).all()
        self.assertEqual(result, expected)




if __name__ == "__main__":
    unittest.main()
