from sqlalchemy import select, delete
from models.products_invoice import ProductsInvoice
from models.customer import Customer
from models.product import Product
from handlers import Session
from utils.flatten_list import flatten


def add_invoice(serial_invoice, customer_object, product_object):
    """Starts session to add invoice, customer and products and automatically ends it"""
    with Session.begin() as sessions:
        invoice = Invoice()
        customer = select(Customer.serial(customer_object)) #How to make customer objects 
        products = select(Product.serial(product_object))   #How to make product objects times X
        invoice.customer.products.append() # append what?



