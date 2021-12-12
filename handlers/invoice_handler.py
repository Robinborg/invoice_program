from sqlalchemy import select, delete
from models.invoice import Invoice
from handlers import Session


def add_invoice(filled_invoice):
    """Starts session to add invoice and automatically ends it"""
    with Session.begin() as session:
        session.add(filled_invoice)
        session.commit()

def all_invoices():
    """Starts session to show all invoices and automatically ends it"""
    with Session.begin() as session:
        statement = select(Invoice.id, Invoice.customer_id,
                           Invoice.product_invoice_relationship,
                           Invoice.customer_relationship)
        result = session.execute(statement).all()
        for row in result:
            print(row)

def remove_invoice(number_invoice_id):
    """Starts session to remove invoice and automatically ends it"""
    with Session.begin() as session:
        statement = delete(Invoice).where(Invoice.id == number_invoice_id).\
                execution_options(synchronize_session='fetch')
        session.execute(statement)

def show_invoice(number_invoice_id):
    """Starts session to show a invoice and automatically ends it"""
    with Session.begin() as session:
        statement = select(Invoice.id).filter_by(id=number_invoice_id)
        result = session.execute(statement).all()
        print(result)

def get_invoice(number_invoice_id):
    """Starts session to show a invoice and automatically ends it"""
    with Session.begin() as session:
        statement = select(Invoice.id, Invoice.customer_id,
                           Invoice.product_invoice_relationship,
                           Invoice.customer_relationship)
        result = session.execute(statement).all()
    return result 
