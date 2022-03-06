from sqlalchemy import select, delete
from models.invoice import Invoice
from models.products_invoice import ProductsInvoice
from models.customer import Customer
from models import Base, Session
from utils.flatten_list import flatten


def add_invoice(filled_invoice: Invoice):
    """Starts session to add invoice and automatically ends it"""
    with Session.begin() as session:
        session.add(filled_invoice)
        session.commit()

def all_invoices():
    """Starts session to show all invoices and automatically ends it"""
    with Session.begin() as session:
        stmt = select(Invoice.id,
                      Invoice.serial,
                      Invoice.customer_id,
                      Invoice.products_invoice_relationship).\
                      join(Invoice.products_invoice_relationship)
        result = session.execute(stmt).all()
        print(result)


def remove_invoice(serial_for_invoice: str):
    """Starts session to remove invoice and automatically ends it"""
    with Session.begin() as session:
        statement = delete(Invoice).where(Invoice.serial == serial_for_invoice).\
                execution_options(synchronize_session='fetch')
        session.execute(statement)

def show_invoice(serial_for_invoice: str):
    """Starts session to show an invoice and automatically ends it"""
    with Session.begin() as session:
        statement = select(Invoice.id,
                           Invoice.serial,
                           Invoice.customer_relationship,
                           Invoice.products_invoice_relationship).where(Invoice.serial == serial_for_invoice).join(Invoice.products_invoice_relationship)
        result = session.execute(statement).all()
        print(result)

def get_invoice_serial()->int:
    """Starts session to show a invoice and automatically ends it"""
    with Session.begin() as session:
        statement = select(Invoice.serial)
        result = session.execute(statement).all()
        print(result)
        if not result:
            return 1000
        result = flatten(result)
        result = list(result)
        result = int(result[-1])
        return result
