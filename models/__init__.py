"""Start the engine, Session and Base for SQLalchemy. Generate the schema for
   Product, Customer, Invoice, ProductsInvoice"""
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine



db_uri = "sqlite:///invoices.db"
engine = create_engine(db_uri, echo=True)

Base = declarative_base()


Base.metadata.create_all(engine)
Session = sessionmaker(engine)

from models.product import Product
from models.customer import Customer
from models.invoice import Invoice
from models.products_invoice import ProductsInvoice
