'''Generate invoices'''

from invoice import InvoiceTemplate
from working_data import FetchAndTransform

first_invoice = InvoiceTemplate("1")
modify_data = FetchAndTransform()
#make_table = modify_data.working_table()
#first_invoice.make_data_table(modify_data.working_table())

#first_invoice.create_document()
#first_invoice.save_pdf()


#modify_data.removing_row(delete_all=True)
modify_data.adding_customer_details("Sam", "samstreet", 1234567)
modify_data.adding_product_details(123, "Wrench", 7)
modify_data.show_table()
