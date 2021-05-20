import pandas as pd
import numpy as np

from reportlab.pdfgen import canvas

'''
    1. Make a pandas dataframe for products
    2. Make a pandas dataframe for customers
    3. Make a pandas dataframe for suppliers
    4. Make an invoice template (Reportlab)
    5. Fetch data from customers dataframe and products dataframe for invoice
    6. Launch a server
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


#pandas_to_list = [suppliers.columns[:,].values.astype(str).tolist()] + suppliers.values.tolist()

#Creating the canvas
c = canvas.Canvas("receipt.pdf",pagesize=(200,250), bottomup=0)
#Creating the logo
c.translate(10,40)
c.scale(1, -1)
c.drawImage("logo.jpg", 0, 0, width=50, height=30)


#Title section
c.scale(1, -1)
c.setFont("Helvetica-Bold", 10)
c.drawCentredString(125, 20, "Oomph Technology Ab Oy")
c.line(70,22,180, 22)
c.setFont("Helvetica-Bold", 5)
c.drawCentredString(125,30, "Address xyz")
c.drawCentredString(125, 35, "Postal number 123")
c.setFont("Helvetica-Bold", 6)
c.drawCentredString(125, 42, "Business ID: ")
c.line(5, 45, 195, 45)

c.setFont("Courier-Bold", 8)
c.drawCentredString(100, 55, "Invoice")

c.roundRect(15, 63, 170, 40, 10, stroke=1, fill=0)
c.setFont("Times-Bold", 5)
c.drawRightString(70, 70, "Invoice number: " )
c.drawRightString(70,80, "Date: ")
c.drawRightString(70,90, "Customer name: ")
c.drawRightString(70, 100, "Phone number: ")

c.roundRect(15, 108, 170, 130, 10, stroke=1, fill=0)
c.line(15, 120, 185, 120)
c.drawCentredString(25, 118, "Serial number: ")
c.drawCentredString(75, 118, "Goods description: ")
c.drawCentredString(125, 118, "Rate: ")
c.drawCentredString(148, 118, "QTY: ")
c.drawCentredString(173, 118, "Total: ")

c.line(15, 210, 185, 210)
c.line(35, 108, 35, 220)
c.line(115, 108, 115, 220)
c.line(135, 108, 135, 220)
c.line(160, 108, 160, 220)

c.line(15, 220, 185, 220)
c.line(100, 220, 100, 238)
c.drawString(20, 225, "We declare that above mentioned")
c.drawString(20, 230, "information is true")
c.drawString(20, 235, "(This system generated invoice)")
c.drawRightString(180, 235, "Authorised signatory")

c.showPage()
c.save()


