#Fetch information from database and output information required for the invoice

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from typing import List


class FetchAndTransform:
    def __init__(self):
        '''creating the engine and fetching the current products and customers'''
        self.engine = create_engine('sqlite:///invoice.db')
        self.products = pd.read_sql('products', self.engine)
        self.customers = pd.read_sql('customers', self.engine)

    def working_table(self, product_number=0) -> List:
        '''loading the data into a table for the invoice'''
        if product_number:
            add_table_products = self.products.iloc[product_number]
        table_data = [
                add_table_products,
            ['Serial', 'Goods and description', 'Rate', 'QTY', 'Total'],       
            ]
        return table_data

    def adding_customer_details(self, customer=0):
        pass


    def adding_to_database(self, new_product=None, new_customer=None):
        if new_product:
            product_number =  1
            product_name = new_product
            product_combined = pd.DataFrame({"name": [product_name], "product number": [product_number]}, index=[product_number])
            self.products.append(product_combined, ignore_index=True)

            self.products.to_sql('products', self.engine, if_exists='append')
            print(self.products)

        elif new_customer:
            customer_number = 1
            customer_name = new_customer
            customers_combined = pd.DataFrame({"name": [customer_name], "customer number": [customer_number]}, index=[customer_number])
            self.customers.append(customers_combined, ignore_index=True)
            
            self.customers.to_sql('customers', self.engine, if_exists='append')
            print(self.customers)

        else:
            print("Enter product=your_choice or customer = your_choice")

    def removing_row(self, remove_product=None, remove_customer=None, delete_all=None):
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
        elif delete_all:
            self.customers = pd.DataFrame()
            self.products = pd.DataFrame()
        else:
            print("Enter remove_product = your_choice or remove_customer = your_choice")

        self.customers.to_sql('customers', self.engine, if_exists='replace')
        self.products.to_sql('products', self.engine, if_exists='replace')
        

    def show_table(self):
        '''print the whole table from sqlite3'''
        self.products
        print(self.products)
        self.customers
        print(self.customers)




