import pandas as pd
import numpy as np

'''
    1. Make a pandas dataframe for products
    2. Make a pandas dataframe for customers
    3. Make a pandas dataframe for suppliers
    4. Make an invoice template (Make it in html?) 
    5. Fetch data from customers dataframe and products dataframe for invoice
    6. Update to a server
'''

products = pd.DataFrame(
        { 
            "product1" : [10000],
            "product2" : [10001],
            "product3" : [10002],
            "product4" : [10003],
            "product5" : [10004],
        }
    )
customers = pd.DataFrame(
        {
            "customer1" :[100],
            "customer2" :[101],
            "customer3" :[102],
            "customer4" :[103],
            "customer5" :[104],
        }
    )
suppliers = pd.DataFrame(
        {
            "supplier1" :[10],
            "supplier2" :[11],
            "supplier3" :[12],
            "supplier4" :[13],
            "supplier5" :[14],
        }
    )

print(suppliers.head())
   
def new_customer():
    customer_number = #last entry + 1
    customer_name = input("Name of customer: ")
    #Add a new customer column to df 
 def new_product():                                                          
     product_number = #last entry + 1                                       
     prodcut_name = input("Name of the product: ")
     #Add a new product column to df

def new_supplier():
    supplier_number = #last entry + 1
    supplier_name = input("Name of supplier: ")
    #Add a new supplier column to df 
