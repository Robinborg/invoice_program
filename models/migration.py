from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

engine = create_engine("sqlite:///invoices.db")
Base.metadata.create_all(engine)
