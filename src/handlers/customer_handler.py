from sqlalchemy import select, delete
from models.customer import Customer
from models import Base, Session
from utils.flatten_list import flatten


def add_customer(customer_object):
    """Starts session to add customer and automatically ends it"""
    with Session.begin() as session:
        session.add(customer_object)
        session.commit()

def all_customers():
    """Starts session to show all customers and automatically ends it"""
    with Session.begin() as session:
        statement = select(Customer.name,\
                Customer.address, Customer.phone)
        result = session.execute(statement).all()
        for row in result:
            print(row)

def remove_customer(name_customer): 
    """Starts session to remove customer and automatically ends it"""
    with Session.begin() as session:
        statement = delete(Customer).where(Customer.name == name_customer).\
                execution_options(synchronize_session='fetch')
        session.execute(statement)

def show_customer(name_customer):
    """Starts session to show a customer and automatically ends it"""
    with Session.begin() as session:
        statement = select(Customer.name, Customer.address, Customer.phone).filter_by(name=name_customer)
        result = session.execute(statement).all()
        print(result)

def get_customer(name_customer):
    """Starts session to show a customer and automatically ends it"""
    with Session.begin() as session:
        statement = select(Customer.name, Customer.address, Customer.phone).filter_by(name=name_customer)
        result = session.execute(statement).all()
        customer_iterable = flatten(result)
        customer_list = list(customer_iterable)
        return customer_list
