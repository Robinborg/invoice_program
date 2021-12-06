from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Association(Base):
    __tablename__ = "association"

    product_id = Column(ForeignKey("product.id"), primary_key=True)
    customer_id = Column(ForeignKey("customer.id"), primary_key=True)
    creation_date = Column(String(250))
    company_name = Column(String(500))
    company_address = Column(String(500))
    company_bussines_id = Column(String(500))
    company = Column(String(500))
    customer_name = Column(String(500))
    customer_serial = Column(String(500))
    customer_address = Column(String(500))
    customer_phone = Column(String(500))
    product_serial = Column(String(500))
    product_description = Column(String(500))
    product_rate = Column(String(500))
    product_quantity = Column(String(500))
    product_total = Column(String(500))

class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    children = relationship("Association", back_populates="invoice")
