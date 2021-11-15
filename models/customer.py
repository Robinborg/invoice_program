import os 
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Customers(Base):
    __tablename__ = 'Customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    company = Column(String(250), nullable=False)
    address = Column(String(500), nullable=False)
    phone = Column(Integer, nullable=False)

engine = create_engine("sqlite:///invoices.db")
#Create the table 
Base.metadata.create_all(engine)
