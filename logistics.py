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

#products = pd.DataFrame(
#        { 
#            "product1" : [10000],
#            "product2" : [20000],
#            "product3" : [30000],
#            "product4" : [40000],
#            "product5" : [50000],
#        }
#    )
#customers = pd.DataFrame(
#        {
#            "customer1" :[100],
#            "customer2" :[200],
#            "customer3" :[300],
#            "customer4" :[400],
#            "customer5" :[500],
#        }
#    )
#suppliers = pd.DataFrame(
#        {
#            "supplier1" :[10],
#            "supplier2" :[20],
#            "supplier3" :[30],
#            "supplier4" :[40],
#            "supplier5" :[50],
#        }
#    )
#
#print(products.loc[0])

#class Logistics():
#
#   def add_products():
#       new_product = input("what product name: ")
#       new_proudct_number = products. 
#
#   def change_products():
#       pass
#   def add_customers():
#       pass
#   def change_customers():
#       pass
#   def add_suppliers():
#       pass
#   def change_suppliers():
#       pass
#   def write_to_pdf():
#       pass
#   

customers = {
        "customer1" : 10000, "customer2" : 10001, "customer3" : 10003, "customer4" : 10004, "customer5" : 10005,
        }
def add_customer():
    new_customer = input("Name of new customer: ")
    new_number = input("Number for customer: ")
    customers[new_customer] = new_number

add_customer()
print(customers)
