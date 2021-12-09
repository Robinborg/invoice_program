from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.orm import relationship, declarative_base
from customer import Customer

Base = declarative_base()

class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key = True)
    products = relationship("ProductsInvoice", backref = "invoices")
    customers = relationship("Customer", backref = "invoices")

