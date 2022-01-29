from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from models import Base


class Product(Base):
    """Make model for a product and name table products"""
    __tablename__ = 'product_table'
    id = Column(Integer)
    serial = Column(String(250), primary_key=True)
    description = Column(String(250), nullable=False)
    price = Column(String(500))
    products_invoice_relationship = relationship("ProductsInvoice",
                                                  back_populates="product_relationship")
    def __eq__(self, other):
        return isinstance(other, Product) and other.id == self.id


