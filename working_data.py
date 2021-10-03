#Fetch information from database and output information required for the invoice

import pandas as pd
import numpy as np
from sqlalchemy import create_engine


class FetchAndTransform:
    def __init__(self):
        '''creating the engine and fetching the current products and customers'''
        engine = create_engine('sqlite:///invoice.db')
        self.products = pd.read_sql('products', engine)
        self.customers = pd.read_sql('customers', engine)

    def working_table(self, add_product=None, add_customer=None):
        '''loading the data into a table for the invoice'''
        table_data = [
                product,
                customer,
            ['Serial', 'Goods and description', 'Rate', 'QTY', 'Total'],       
            ]
        return table_data

    def adding_to_database(self,new_prouct=None, new_customer=None):
        if new_product:
            product_number = self.products.iloc[-1, -1] + 1
            product_name = product
            products[product_name] = product_number
        elif new_customer:
            customer_number = self.customers.iloc[-1, -1] + 1
            customer_name = customer
            customers[customer_name] = customer_number
        else:
            print("Enter product=your_choice or customer = your_choice")

        self.products.to_sql('products', self.engine)
        self.customers.to_sql('customers', self.engine)

    def removing_row(self, remove_product=None, remove_customer=None):
        '''removing products or customers'''
        if remove_product == "product":
            del self.products['product2']
            del self.products['product1']
            del self.products['product3']
            del self.products['product4']
            del self.products['product5']
            print(self.products)
        elif remove_customer == "customer":
            self.customers.drop(len(self.customers)-1)
            print(self.customers)
        else:
            print("Enter remove_product = your_choice or remove_customer = your_choice")

        self.customers.to_sql('customers', engine)
        self.products.to_sql('products', engine)





