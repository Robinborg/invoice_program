'''Generate invoices'''

from invoice import InvoiceTemplate
#from working_data import Fetch_and_transform
#from working_data import fetch_client, fetch_product

first_invoice = InvoiceTemplate("1")
first_invoice.create_document()
first_invoice.save_pdf()
#retrieve_data = Fetch_and_Transform.fetch_client()
#retrieve_data.fetch_client()
#retrieve_data.fetch_products()



