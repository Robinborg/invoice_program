from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key = True)
    products = relationship("ProductsInvoice", back_populates = "invoice")
    customers = relationship("Customer", back_populates = "invoice")

