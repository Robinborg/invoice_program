from sqlalchemy import select, delete, update
from models.customer import Customer
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
        count = 0
        for row in result:
            print(row)
            print(count)
            count += 1

def removing_customer(delete_customer: str = None):
    """Starts session to remove customer and automatically ends it"""
    with Session.begin() as session:
        stmt = delete(Customer).where(Customer.first_name == delete_customer).\
                execution_options(synchronize_session='fetch')
        session.execute(stmt)

def show_customer(search_customer):
    """Starts session to show a customer and automatically ends it"""
    with Session.begin() as session:
        stmt = select(Customer).where(Customer.first_name == search_customer).\
                execution_options(synchronize_session='fetch')
        result = session.execute(stmt).all()
        print(result)

