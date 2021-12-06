import os 
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Customer(Base):
    """Declare base for Customer class"""
    __tablename__ = 'Customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(500), nullable=False)
    phone = Column(String(250), nullable=False)
    parents = relationsship("Association", back_populates="customer")

#To be ran only once
engine = create_engine("sqlite:///invoices.db")
#To be ran only once
#Create the table
Base.metadata.create_all(engine)
