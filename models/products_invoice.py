from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class ProductsInvoice(Base):
    __tablename__ = "products_invoice"

    product_id = Column(ForeignKey("products.id"), primary_key = True)
    product_serial = Column(String(500))
    product_description = Column(String(500))
    product_rate = Column(String(500))
    product_quantity = Column(String(500))
    product_total = Column(String(500))

