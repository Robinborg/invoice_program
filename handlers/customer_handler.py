from sqlalchemy import select, delete, update
from models.customer import Customer
from handlers import Session
from utils.flatten_list import flatten


def adding_customer(add_customer):
    """Starts session to add customer and automatically ends it"""
    with Session.begin() as session:
        session.add(add_customer)
        session.commit()

def all_customers():
    """Starts session to show all customers and automatically ends it"""
    with Session.begin() as session:
        statement = select(Customer.name,\
                Customer.address, Customer.phone)
        result = session.execute(statement).all()
        for row in result:
            print(row)

def removing_customer(delete_customer: str = None):
    """Starts session to remove customer and automatically ends it"""
    with Session.begin() as session:
        stmt = delete(Customer).where(Customer.name == delete_customer).\
                execution_options(synchronize_session='fetch')
        session.execute(stmt)

def show_customer(search_customer):
    """Starts session to show a customer and automatically ends it"""
    with Session.begin() as session:
        stmt = select(Customer.name).filter_by(name=search_customer)
        result = session.execute(stmt).all()
        print(result)
        return result

def get_customer(search_customer):
    """Starts session to show a customer and automatically ends it"""
    with Session.begin() as session:
        stmt = select(Customer.name, Customer.address, Customer.phone).filter_by(name=search_customer)
        result = session.execute(stmt).all()
        customer_iterable = flatten(result)
        print(customer_iterable)
        customer_list = list(customer_iterable)
        print(customer_list)
        return customer_list
