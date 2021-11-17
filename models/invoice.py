import os 
import sys
from sqlalchemy import Column, ForeigKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine

Base = declarative_base()

class Invoices(Base):
    __tablename__ = 'Invoices'
    id = Column(Integer, primary_key=True)
    invoice_id = Column("invoice_id", Integer, ForeignKey("invoice.invoice_id")
    customer = relationship("Customer", backref=backref("invoices"))
    product = relationship("Product", backref=backref("invoices"))

    def __repr__(self):
    return f"Invoice {self.id} {self.customer}"

#To be ran only once
engine = create_engine("sqlite:///invoices.db")
#To be ran only once
#Create table 
Base.metadata.create_all(engine)



