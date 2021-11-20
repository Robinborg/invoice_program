from models.customer import Customer
from handlers import Session

class CustomerHandler:
    __tablename__ = 'customers'

    def get_all_customers(self, enter_session):
        enter_session.query(customers).all()

    def add_one_customer(self, enter_session):
        enter_session.query(customers).add_entity()

    def remove(self, enter_session):
        enter_session.query(customers).delete()

    def search(self, enter_session):
        enter_session.query(customers).get(looking_for)

#NOTE: either add the argument to be modified from class or function?
def adding_customer(add_customer, enter_session=None):
    """Starts session to add customer and automatically ends it"""
    with Session.begin() as session:
        CustomerHandler.add_one_customer(add_customer, enter_session=session)
        session.commit()

def showing_all(show_all, enter_session=None):
    """Starts session to show all customers and automatically ends it"""
    with Session.begin() as session:
        CustomerHandler.get_all_customers(enter_session=session)
        session.commit()

def removing_customer(remove_customer, enter_session=None):
    """Starts session to remove customer and automatically ends it"""
    with Session.begin() as session:
        CustomerHandler.remove(remove_customer, enter_session=session)
        session.commit()

def show_customer(search_customer, enter_session=None):
    """Starts session to show a customer and automatically ends it"""
    with Session.begin() as session:
        CustomerHandler.search(search_customer, enter_session=session)
        session.commit()
