from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from models import Base


class Customer(Base):
    """Declare base for Customer class"""
    __tablename__ = 'customer_table'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(500), nullable=False)
    phone = Column(String(250), nullable=False)
    invoice_relationship = relationship("Invoice",
                                        back_populates="customer_relationship", viewonly=True)


