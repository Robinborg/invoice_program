"""
Start the engine, Session and Base for SQLalchemy.
Generate the schema for Product, Customer, Invoice, ProductsInvoice
"""
import sys
from os import path
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

file_name = "invoices.db"
file_path = '/invoice_program/src'

if not path.isfile(file_name):
    print("failed to locate server \n",
          "Try running load_database.py")

if not path.exists(file_path):
    print("path is not defined")

#uri for engine
db_uri = f"sqlite:///{file_path}/{file_name}"
#start engine for sqlalchemy and echo=True for SQL output
engine = create_engine(db_uri, echo=True)
#Set declarative_base for the ORMs 
Base = declarative_base()

#Create schema
Base.metadata.create_all(engine)

#Create Session for all the modules
Session = sessionmaker(engine)

#import all the ORMs so they are created correctly
from models.product import Product
from models.customer import Customer
from models.invoice import Invoice
from models.products_invoice import ProductsInvoice
