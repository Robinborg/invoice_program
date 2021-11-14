'''Generate invoices'''

from invoice import InvoiceTemplate
from handling_data import FetchAndTransform
import sys

#Make default number
if __name__ == "__main__":
    first_invoice = InvoiceTemplate("2")
    modify_data = FetchAndTransform()
    make_table = modify_data.working_table(select_index=1, quantity=2)
    #print(make_table)
    first_invoice.make_data_table(make_table)
    #modify_data.removing_row(delete_all=False)
    #modify_data.adding_customer_details("George", "Starbase", 9999)
    #modify_data.adding_product_details(serial=100, description="Hammer", rate=15)
    #modify_data.show_table()
    customer_details = modify_data.working_customer_info(1)
    first_invoice.create_document(invoice_number=2,
            customer_name = customer_details[0], customer_phone = customer_details[2])
    first_invoice.save_pdf()
#    while True:
#        enter_command = input("Enter instruction: ")
#        if enter_command.lower() == 'quit':
#            break
#        elif enter_command.lower() == "add product":
#            add_product_serial= input("Enter product serial: ")
#            add_product_goods_description = input("Enter product goods and description: ")
#            add_product_rate= input("Enter product rate: ")
#            modify_data.adding_product_details(add_product_serial,
#                    add_product_goods_description, add_product_rate)
#            continue
#        elif enter_command.lower() == 'add customer':
#            add_customer_name = input("Enter customer name: ")
#            add_customer_address = input("Enter customer address: ")
#            add_customer_phone = input("Enter customer phone: ")
#            modify_data.adding_customer_details(add_customer_name, add_customer_address,
#                    add_customer_phone)
#            continue
#
