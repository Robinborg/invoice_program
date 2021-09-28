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
        client_information = []
        product_information = []
    def working_table(self):
        table_data = [
            ['10000', 'wrench', '10', '1', '10'],
            ['20000', 'screwdriver', '20', '2', '40'],
            ['30000', 'hammer', '5', '1', '5'],
            ['Serial', 'Goods and description', 'Rate', 'QTY', 'Total'],       
            ]
        return table_data







engine = create_engine('sqlite:///invoice.db')

products = pd.read_sql('products', engine)
customers = pd.read_sql('customers', engine)
suppliers = pd.read_sql('customers', engine)

table_data = [
        ['Serial', 'Goods and description', 'Rate', 'QTY', 'Total'],
        ['10000', 'wrench', '10', '1', '10'],
        ['20000', 'screwdriver', '20', '2', '40'],
        ['30000', 'hammer', '5', '1', '5']
        ]

