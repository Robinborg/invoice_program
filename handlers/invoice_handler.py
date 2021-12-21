from sqlalchemy import select, delete
from models.invoice import Invoice
from models import Base, Session
from utils.flatten_list import flatten


def add_invoice(filled_invoice):
    """Starts session to add invoice and automatically ends it"""
    with Session.begin() as session:
        session.add(filled_invoice)
        session.commit()

def all_invoices():
    """Starts session to show all invoices and automatically ends it"""
    with Session.begin() as session:
        statement = select(Invoice.id,
                           Invoice.serial,
                           Invoice.customer_id,
                           Invoice.products_invoice_relationship)
        result = session.execute(statement).all()
        for row in result:
            print(row)

def remove_invoice(serial_for_invoice):
    """Starts session to remove invoice and automatically ends it"""
    with Session.begin() as session:
        statement = delete(Invoice).where(Invoice.serial == serial_for_invoice).\
                execution_options(synchronize_session='fetch')
        session.execute(statement)

def show_invoice(serial_for_invoice):
    """Starts session to show a invoice and automatically ends it"""
    with Session.begin() as session:
        statement = select(Invoice.serial).where(Invoice.serial == serial_for_invoice)
        result = session.execute(statement).all()
        print(result)

def get_invoice_serial():
    """Starts session to show a invoice and automatically ends it"""
    with Session.begin() as session:
        statement = select(Invoice.serial)
        result = session.execute(statement).all()
        result = flatten(result)
        print(result)
        print(type(result))
        result = list(result)
        print(result)
        result = int(result[-1])
        print(type(result))
    return result
