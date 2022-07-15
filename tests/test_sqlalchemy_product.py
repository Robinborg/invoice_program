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

class TestQuery(unittest.TestCase):

    engine = create_engine("sqlite:///invoices.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    
    def setUp(self):
        Base.metadata.create_all(self.engine)
        self.product = Product(serial = "1",
                               description ="hammer",
                               price = "100")
        self.session.add(self.product)
        self.session.commit()

    def teardown(self):
        Base.metadata.drop_all(self.engine)


    def test_query_product(self):
        expected = [self.product]
        result = self.session.query(Product).all()
        self.assertEqual(result, expected)




if __name__ == "__main__":
    unittest.main()
