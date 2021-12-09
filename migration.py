from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.orm import relationship, declarative_base
from models.customer import Customer
from models.product import Product
from models.invoice import Invoice
from models.products_invoice import ProductsInvoice


Customer()
Product()
Invoice()
ProductsInvoice()

Base = declarative_base()

engine = create_engine("sqlite:///invoices.db")
Base.metadata.create_all(engine)
