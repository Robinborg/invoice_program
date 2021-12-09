from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.orm import relationship, declarative_base
from models.product import Product
from models.invoice import Invoice
from models.customer import Customer
from models.products_invoice import ProductsInvoice

customer = Customer()
product = Product()
invoice = Invoice()
products_invoice = ProductsInvoice()

Base = declarative_base()

engine = create_engine("sqlite:///invoices.db")
Base.metadata.create_all(engine)
