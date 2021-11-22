from sqlalchemy import select
from models.customer import Customer
from models.customer import Base
from handlers import Session


def adding_customer(add_customer):
    """Starts session to add customer and automatically ends it"""
    with Session.begin() as session:
        session.add(add_customer)
        session.commit()

def all_customers():
    """Starts session to show all customers and automatically ends it"""
    with Session.begin() as session:
        statement = select(Customer.first_name)
        result = session.execute(statement).all()
        for row in result:
            print(row)

def removing_customer(remove_customer):
    """Starts session to remove customer and automatically ends it"""
    with Session.begin() as session:
        session.execute(Customer.first_name.delete())
        session.commit(stmt)

def show_customer(search_customer):
    """Starts session to show a customer and automatically ends it"""
    with Session.begin() as session:
        statement = select(Customer).filter_by(first_name=search_customer)
        session.execute(statement).all()

