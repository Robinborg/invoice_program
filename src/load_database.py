from models import *


uri = ("sqlite:///invoices.db")
engine = create_engine(uri)
Base.metadata.create_all(engine)

