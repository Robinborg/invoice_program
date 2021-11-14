import os 
import sys
from sqlalchemy import Column, ForeigKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Products:
    __tablename__ = 'Products'
    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=False)
    price = Column(Integer)

engine = create_engine("sqlite:///invoices.db")
#Create table 
Base.metadata.create_all(engine)



