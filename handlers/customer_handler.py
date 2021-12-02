from sqlalchemy import select, delete
from models.customer import Customer
from handlers import Session
from utils.flatten_list import flatten


def add_customer(name_customer):
    """Starts session to add customer and automatically ends it"""
    with Session.begin() as session:
        session.add(name_customer)
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
        stmt = delete(Customer).where(Customer.name == name_customer).\
                execution_options(synchronize_session='fetch')
        session.execute(stmt)

def show_customer(name_customer):
    """Starts session to show a customer and automatically ends it"""
    with Session.begin() as session:
        stmt = select(Customer.name, Customer.address, Customer.phone).filter_by(name=name_customer)
        result = session.execute(stmt).all()
        print(result)

def get_customer(name_customer):
    """Starts session to show a customer and automatically ends it"""
    with Session.begin() as session:
        stmt = select(Customer.name, Customer.address, Customer.phone).filter_by(name=name_customer)
        result = session.execute(stmt).all()
        customer_iterable = flatten(result)
        customer_list = list(customer_iterable)
        return customer_list
