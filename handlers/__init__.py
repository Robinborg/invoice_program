from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///invoice.db")

Session = sessionmaker(engine, future=True)

