from sqlalchemy import select, delete
from models.product import Product
from handlers import Session
from utils.flatten_list import flatten


def add_product(name_product):
    """Starts session to add product and automatically ends it"""
    with Session.begin() as session:
        session.add(name_product)
        session.commit()

def all_products():
    """Starts session to show all products and automatically ends it"""
    with Session.begin() as session:
        statement = select(Product.serial, Product.description, Product.price)
        result = session.execute(statement).all()
        for row in result:
            print(row)

def remove_product(name_product: str = None):
    """Starts session to remove product and automatically ends it"""
    with Session.begin() as session:
        statement = delete(Product).where(Product.description == name_product).\
                execution_options(synchronize_session='fetch')
        session.execute(statement)

def show_product(name_product):
    """Starts session to show a product and automatically ends it"""
    with Session.begin() as session:
        statement = select(Product.description).filter_by(description=name_product)
        result = session.execute(statement).all()
        print(result)

def get_product(name_product):
    """Starts session to show a product and automatically ends it"""
    with Session.begin() as session:
        statement = select(Product.serial, Product.description, Product.price).filter_by(description=name_product)
        result = session.execute(statement).all()
        product_list = list(flatten(result))
    return product_list
