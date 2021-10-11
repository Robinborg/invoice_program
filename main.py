'''Generate invoices'''

from invoice import InvoiceTemplate
from working_data import FetchAndTransform

first_invoice = InvoiceTemplate("1")
modify_data = FetchAndTransform()
#make_table = modify_data.working_table(1)
#first_invoice.make_data_table(make_table)
#modify_data.removing_row(delete_all='yes')
modify_data.adding_to_database(new_product='first_product')
modify_data.adding_to_database(new_customer='first_customer')
#modify_data.show_table()
#first_invoice.create_document(1000000)

#first_invoice.save_pdf()


