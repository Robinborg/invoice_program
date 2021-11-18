import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///invoice.db")
link_database = sessionmaker(bind=engine)     

