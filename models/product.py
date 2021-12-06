from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Product(Base):
    """Make model for a product and name table products"""
    __tablename__ = 'Products'

    id = Column(Integer, primary_key=True)
    serial = Column(String(250))
    description = Column(String(250), nullable=False)
    price = Column(String(500))
    parents = relationship("Association", back_populates="product")

#To be ran only once
#engine = create_engine("sqlite:///invoices.db")
#To be ran only once
#Create table 
#Base.metadata.create_all(engine)

