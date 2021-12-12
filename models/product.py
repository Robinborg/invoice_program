from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Product(Base):
    """Make model for a product and name table products"""
    __tablename__ = 'product_table'
    id = Column(Integer, primary_key=True)
    serial = Column(String(250))
    description = Column(String(250), nullable=False)
    price = Column(String(500))
    products_invoice_id = Column(ForeignKey("products_invoice_table.id"))
    products_invoice_relationship = relationship("ProductsInvoice",
                                                  back_populates="product_relationship")


