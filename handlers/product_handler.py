from sqlalchemy import select

from handlers import Session


def adding_product(add_product, enter_session=None):
    """Starts session to add product and automatically ends it"""
    with Session.begin() as session:
        session.add(add_product)
        session.commit()

def showing_all(show_all, enter_session=None):
    """Starts session to show all products and automatically ends it"""
    with Session.begin() as session:
        statement = select(Product.description)
        session.execute(statement).all()

def removing_product(remove_product, enter_session=None):
    """Starts session to remove product and automatically ends it"""
    with Session.begin() as session:
        session.delete(remove_product)
        session.commit()

def show_product(search_product, enter_session=None):
    """Starts session to show a product and automatically ends it"""
    with Session.begin() as session:
        statement = select(Product).filter_by(first_name=search_product)
        session.execute(statement).all()

