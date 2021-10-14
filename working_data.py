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

    def working_table(self):
        '''loading the data into a table for the invoice'''
        add_table_products = self.products.iloc[0]
        converted_list = add_table_products.values.tolist()
        strings_list = [str(x) for x in converted_list]
        #add_table_products = [item for sub_list in add_table_products for item in sub_list]
        table_data = [
                strings_list,
            ['Serial', 'Goods and description', 'Rate', 'Total'],       
            ]
        return table_data

    def adding_customer_details(self, customer_name: str=None, customer_address: str=None, customer_phone: int=0):
        customer_details = {"Name": [customer_name], "Address": [customer_address], "Phone number": [customer_phone]}
        self.customers.append(customer_details, ignore_index=True)
        self.customers.to_sql("customers", self.engine, if_exists="replace")

    def adding_to_database(self, new_product=None, new_customer=None):
        if new_product:
            self.product_number = self.products.iloc[-1, -1] + 1 
            self.product_name = new_product
            self.products_combined = pd.DataFrame({"name": [self.product_name], "product number": [self.product_number]})
            self.products.append(self.products_combined, ignore_index=True)
            self.products.to_sql("products", self.engine, if_exists="replace")
        else:
            print("Enter product=your_choice")

    def removing_row(self, remove_product=None, remove_customer=None, delete_all=None):
        '''removing products or customers'''
        if remove_product == "product":
            del self.products[remove_product]
            print(self.products)
        elif remove_customer == "customer":
            del self.customers[remove_customer]
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
        print(self.products)
        print(self.customers)




