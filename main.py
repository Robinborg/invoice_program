'''Generate invoices'''

from invoice import InvoiceTemplate
from working_data import FetchAndTransform

first_invoice = InvoiceTemplate("1")
modify_data = FetchAndTransform()
make_table = modify_data.working_table()
first_invoice.make_data_table(modify_data.working_table())

first_invoice.create_document()

first_invoice.save_pdf()


#modify_data.removing_row(remove_product='')
#modify_data.adding_to_database(new_product='first_product')
#modify_data.adding_to_database(new_customer='first_customer')
#modify_data.show_table()
