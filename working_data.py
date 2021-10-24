#Fetch information from database and output information required for the invoice

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from typing import List


class FetchAndTransform:
    def __init__(self):
        """Creating the engine and loading the current products and customers"""
        self.engine = create_engine('sqlite:///invoice.db')
        self.products = pd.read_sql('products', self.engine)
        self.customers = pd.read_sql('customers', self.engine)

    def working_table(self):
        """loading the data into a table for the invoice"""
        add_table_products = self.products.iloc[0]
        converted_list = add_table_products.values.tolist()
        strings_list = [str(x) for x in converted_list]
        table_data = [
                strings_list,
            ['Serial', 'Goods and description', 'Rate', 'Total'],       
            ]
        return table_data

    def adding_customer_details(self, customer_name: str=None, customer_address: str=None, customer_phone: int=0):
        """Adding a new customer to the database"""
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_phone = customer_phone
        self.customer_details = pd.DataFrame({"Name": [customer_name], "Address": [customer_address], "Phone number": [customer_phone]})
        self.customer_details.to_sql("customers", self.engine, if_exists="replace", index=False)

    def adding_product_details(self, serial: int=None, description: str=None,
                           rate: int=None):
        """adding a new product to the the database"""
        self.serial = serial
        self.description = description
        self.rate = rate
        self.products_details = pd.DataFrame({"serial": [self.serial], "goods and description": [self.description], "rate": [self.rate]})
        self.products_details.to_sql("products", self.engine, if_exists="replace", index=False)

    def removing_row(self, remove_product: str=None, remove_customer: str=None, delete_all: str=None):
        """Removing products or customers"""
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
        """Print the whole table from sqlite3"""
        print(self.products)
        print(self.customers)




