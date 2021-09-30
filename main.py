'''Generate invoices'''

from invoice import InvoiceTemplate
from working_data import FetchAndTransform

#first_invoice = InvoiceTemplate("1")
display_data = FetchAndTransform()
#first_invoice.make_data_table(display_data.working_table())
display_data.removing_row(product="product")
#first_invoice.create_document(1000000)

#first_invoice.save_pdf()


