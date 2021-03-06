from sqlalchemy import select, delete
from models.products_invoice import ProductsInvoice
from models import Base, Session


def add_products_invoice(products_invoice_object: ProductsInvoice):
    with Session.begin() as session:
        session.add(products_invoice_object)
        session.commit()

def all_products_invoices():
    with Session.begin() as session:
        statement = select(ProductsInvoice.id,
                            ProductsInvoice.product_id,
                            ProductsInvoice.invoice_id,
                            ProductsInvoice.product_serial,
                            ProductsInvoice.product_description,
                            ProductsInvoice.product_rate,
                            ProductsInvoice.product_quantity,
                            ProductsInvoice.product_total)
        result = session.execute(statement).all()
        print(result)
        return result

def remove_products_invoice(products_invoice_id: str):
    with Session.begin() as session:
        statement = delete(ProductsInvoice.id == products_invoice_id).\
                           execution_options(synchronize_session="fetch")
        session.execute(statement)

def show_products_invoice(products_invoice_id: str):
    with Session.begin() as session:
        statement = select(ProductsInvoice.id,
                            ProductsInvoice.product_id,
                            ProductsInvoice.invoice_id,
                            ProductsInvoice.product_serial,
                            ProductsInvoice.product_description,
                            ProductsInvoice.product_rate,
                            ProductsInvoice.product_quantity,
                            ProductsInvoice.product_total).\
                                            filter_by(id=products_invoice_id)
        result = session.execute(statement).all()
        return result


                                                                     
