#Fetch information from database and output information required for the invoice

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
#Code from db
#engine = create_engine('sqlite3:///invoice.db')
#fetch etc
#get all products and clients needed and store those in the client section and data table


class FetchAndTransform:
    def __init__(self):
        engine = create_engine('sqlite:///invoice.db')
        self.products = pd.read_sql('products', engine)
        self.customers = pd.read_sql('customers', engine)

    def working_table(self):
        table_data = [
            ['Serial', 'Goods and description', 'Rate', 'QTY', 'Total'],       
            ]
        return table_data
    def removing_row(self, product=None, customer=None):
        if product == "product":
            del self.products['product2']
            del self.products['product1']
            del self.products['product3']
            del self.products['product4']
            del self.products['product5']
            print(self.products)
        elif customer == "customer":
            self.customers.drop(len(self.customers)-1)
            print(self.customers)
        else:
            print("You failed to enter product or customer")




