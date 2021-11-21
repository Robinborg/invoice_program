from sqlalchemy import select

from handlers import Session


def adding_customer(add_customer, enter_session=None):
    """Starts session to add customer and automatically ends it"""
    with Session.begin() as session:
        session.add(add_customer)
        session.commit()

def showing_all(show_all, enter_session=None):
    """Starts session to show all customers and automatically ends it"""
    with Session.begin() as session:
        statement = select(Customer.first_name)
        session.execute(statement).all()

def removing_customer(remove_customer, enter_session=None):
    """Starts session to remove customer and automatically ends it"""
    with Session.begin() as session:
        session.delete(remove_customer)
        session.commit()

def show_customer(search_customer, enter_session=None):
    """Starts session to show a customer and automatically ends it"""
    with Session.begin() as session:
        statement = select(Customer).filter_by(first_name=search_customer)
        session.execute(statement).all()

