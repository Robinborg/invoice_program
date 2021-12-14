"""The creation of the schema requires a certain order hence the classes are in this order"""

from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Product(Base):
    """Make model for a product and name table products"""
    __tablename__ = 'product_table'
    id = Column(Integer, primary_key=True)
    serial = Column(String(250))
    description = Column(String(250), nullable=False)
    price = Column(String(500))
    products_invoice_relationship = relationship("ProductsInvoice",
                                                  back_populates="product_relationship")
class Customer(Base):
    """Declare base for Customer class"""
    __tablename__ = 'customer_table'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(500), nullable=False)
    phone = Column(String(250), nullable=False)
    invoice_relationship = relationship("Invoice",
                                        back_populates="customer_relationship")

class Invoice(Base):
    __tablename__ = 'invoice_table'

    id = Column(Integer, primary_key = True)
    customer_id = Column(ForeignKey("customer_table.id"))
    products_invoice_relationship = relationship("ProductsInvoice",
                                                  back_populates = "invoice_relationship")
    customer_relationship = relationship("Customer",
                                         back_populates="invoice_relationship")

class ProductsInvoice(Base):
    __tablename__ = "products_invoice_table"

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey("product_table.id"))
    invoice_id = Column(ForeignKey("invoice_table.id"))
    product_serial = Column(String(500))
    product_description = Column(String(500))
    product_rate = Column(String(500))
    product_quantity = Column(String(500))
    product_total = Column(String(500))
    product_relationship = relationship("Product", back_populates="products_invoice_relationship")
    invoice_relationship = relationship("Invoice", back_populates="products_invoice_relationship")


engine = create_engine("sqlite:///invoices.db")
Base.metadata.create_all(engine)


