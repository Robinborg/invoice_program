from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine



db_uri = "sqlite:///invoices.db"
engine = create_engine(db_uri, echo=True)

Base = declarative_base()

Base.metadata.create_all(engine)
Session = sessionmaker(engine)

from product import Product
from customer import Customer
from invoice import Invoice
from products_invoice import ProductsInvoice


