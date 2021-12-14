'''Generate invoices'''
from invoice import InvoiceTemplate
from models import *
from interface.invoice_menus import product_interface, customer_interface
from interface.product_menus import product_management_loop
from interface.customer_menus import customer_management_loop
from models import Base

#Run to create schema for SQL
from models import create_schema


if __name__ == "__main__":
    while True:
        choose_mode = input("""\t\tEnter:\n\t\t(1). Product mode\n\t\t(2). Customer mode\n\t\t(3). Make invoice\n\t\t(q). Quit\n""")
        if choose_mode == '1':
            product_management_loop()
        elif choose_mode == '2':
            customer_management_loop()
        elif choose_mode == '3':
            products_list = product_interface()
            customer_list = customer_interface()
            make_invoice = InvoiceTemplate("100")
            make_invoice.make_data_table(products_list)
            make_invoice.create_document(invoice_number = 0,
                                           customer_name = customer_list[0],
                                           customer_address = customer_list[1],
                                           customer_phone=customer_list[2])
            make_invoice.save_pdf()
        elif choose_mode == 'q':
            break
        else:
            print("You did not enter the right mode."
                  "Rerun the program and choose 1, 2, 3 or q to quit")

