import os 
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from connection_database import link_database

Base = declarative_base()

class Products(Base):
    __tablename__ = 'Products'
    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=False)
    price = Column(Numeric, nullable=False)

#To be ran only once
engine = create_engine("sqlite:///invoices.db")
#To be ran only once
#Create table 
Base.metadata.create_all(engine)

bridge_db = link_database

first_product = Products(id=1, description='hammer', price=10)
bridge_db.add(first_product)


