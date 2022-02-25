from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.orm import relationship, declarative_base
from models import Base


class ProductsInvoice(Base):
    __tablename__ = "products_invoice_table"

    products_invoice_id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey("product_table.id"))
    invoice_id = Column(ForeignKey("invoice_table.id"))
    product_serial = Column(String(500))
    product_description = Column(String(500))
    product_rate = Column(String(500))
    product_quantity = Column(String(500))
    product_total = Column(String(500))
    product_relationship = relationship(
        "Product",
        back_populates="products_invoice_relationship"
    )
    invoice_relationship = relationship(
        "Invoice",
        back_populates="products_invoice_relationship"
    )


