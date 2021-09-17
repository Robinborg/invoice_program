#Fetch information from database and output information required for the invoice

import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine('sqlite:///invoice.db')

products = pd.read_sql('products', engine)
customers = pd.read_sql('customers', engine)
suppliers = pd.read_sql('customers', engine)



