"""
Start the engine, Session and Base for SQLalchemy.
Generate the schema for Product, Customer, Invoice, ProductsInvoice
"""
from os import path
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine



#uri for engine
db_uri = "sqlite:///invoices.db"
#start engine for sqlalchemy and echo=True for SQL output
engine = create_engine(db_uri, echo=True)
#Set declarative_base for the ORMs 
Base = declarative_base()


#Create schema
file_there = "invoice_program/invoices.db"

if not path.exists(file_there):
    Base.metadata.create_all(engine)
else:
    pass



#Create Session for all the modules
Session = sessionmaker(engine)

#import all the ORMs so they are created correctly
from models.product import Product
from models.customer import Customer
from models.invoice import Invoice
from models.products_invoice import ProductsInvoice
