from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///invoices.db")

Session = sessionmaker(engine, future=True)

