import pandas as pd
import numpy as np

from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

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

#print(suppliers.head())

def new_customer():
    customer_number = customers.iloc[-1, -1] + 1 
    customer_name = input("Name of customer: ")
    customer[customer_name] = customer_number

def new_product():                                                          
    product_number = products.iloc[-1, -1] + 1                                      
    product_name = input("Name of the product: ")
    products[product_name] = product_number

def new_supplier():
    supplier_number = suppliers.iloc[-1, -1] + 1 
    supplier_name = input("Name of supplier: ")
    suppliers[supplier_name] = supplier_number 

#new_supplier()
#print(suppliers)

DATA = [
        ["Date", "Name", "Subscription", "Price"],
        ["09.05.2021"],
        ["Sessions", "", "", ""],
        ["Sub total", "", "", "2000"],
        ["Discount", "", "", "3000"],
        ["Total", "", "", "4000"],

        ]
pandas_to_list = [suppliers.columns[:,].values.astype(str).tolist()] + suppliers.values.tolist()

#Creating a base document template of page size A4
pdf = SimpleDocTemplate("receipt.pdf", pagesize = A4)
#Standard stylesheet defined within reportlab itself
styles = getSampleStyleSheet()
#Fetching the style of top level heading (heading1)
title_style = styles["Heading1"]
#0: left, 1: center, 2: right
title_style.alignment = 1
# Creating the paragraph with the heading text and passing the styles of it
title = Paragraph("Invoice", title_style)
#Create table style object and in it,
#defines the styles row wise,
#the tuples which look like coordinates
#are nothing but rows and columns
style = TableStyle (
        [
            ("BOX", (0,0), (-1, -1), 1, colors.black),
            ("GRID", (0,0), (4,4), 1, colors.black),
            ("BACKGROUND", (0,0), (3, 0), colors.gray),
            ("TEXTCOLOR", (0,0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("BACKGROUND", (0,1), (-1, -1), colors.beige),

            ]
        )
#Creates a table object and passes styles to it
table = Table(pandas_to_list, style=style)
#Final step which builds the actual pd putting together all the elements
pdf.build([title, table])
