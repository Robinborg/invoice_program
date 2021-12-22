"""Manage database and create invoice pdfs"""
from invoice_template import InvoiceTemplate
from interface.invoice_creation_interface import product_interface_for_invoice, \
                                        customer_interface_for_invoice
from interface.product_interface import product_management_loop
from interface.customer_interface import customer_management_loop
from interface.invoice_interface import invoice_management_loop
from handlers.invoice_handler import get_invoice_serial, add_invoice
from models import Product, Customer, ProductsInvoice, Invoice
from utils.quit import quit_loop

if __name__ == "__main__":
    while True:
        enter_mode = input("\t\tEnter:\n\t\t"
                            "(1). Product mode\n\t\t"
                            "(2). Customer mode\n\t\t"
                            "(3). Invoice mode\n\t\t"
                            "(4). Make an invoice\n\t\t"
                            "(q). Quit\n")
        if enter_mode == '1':
            #Manage product database
            product_management_loop()

        elif enter_mode == '2':
            #Manage customer database
            customer_management_loop()

        elif enter_mode == '3':
            #Manage invoice database
            invoice_management_loop()

        elif enter_mode == '4':
            #Fetch products from database to invoice
            products_list = product_interface_for_invoice()
            #Fetch customer from databse to invoice
            customer_list = customer_interface_for_invoice()
            #Break out of invoice creation if None is returned
            if customer_list is None or len(products_list) <= 1:
                break
            #Fill product for database
            product_1 = Product(serial = products_list[0][0],
                                description = products_list[0][1],
                                price = products_list[0][2])
            #Fill customer for database
            customer_1 = Customer(name = customer_list[0],
                                  address = customer_list[1],
                                  phone = customer_list[2])

            #Full list of products for ProductsInvoice
            full_list_of_products_invoices = []
            #Iterate produts_list to append full_list_of_products for ProductsInvoice
            for product_row in range(0, len(products_list)-2):
                products_invoice_list = ProductsInvoice(product_relationship = product_1,
                                                 product_serial = products_list[product_row][0],
                                                 product_description = products_list[product_row][1],
                                                 product_rate = products_list[product_row][2],
                                                 product_quantity = products_list[product_row][3],
                                                 product_total = products_list[product_row][4]
                                                 )
                full_list_of_products_invoices.append(products_invoice_list)
            #Get latest invoice number and add one for the new invoice
            invoice_serial_plus_one = get_invoice_serial() + 1
            #Fill invoice for database
            invoice_1 = Invoice(serial = invoice_serial_plus_one,
                                customer_relationship = customer_1,
                                products_invoice_relationship = full_list_of_products_invoices)
            #Add invoice to database
            add_invoice(invoice_1)

            #Create the invoice PDF
            make_invoice = InvoiceTemplate(str(invoice_serial_plus_one))
            make_invoice.make_data_table(products_list)
            make_invoice.create_document(invoice_number = invoice_serial_plus_one,
                                           customer_name = customer_list[0],
                                           customer_address = customer_list[1],
                                           customer_phone=customer_list[2])
            make_invoice.save_pdf()
        elif quit_loop(enter_mode):
            break
        else:
            print("You did not enter the right mode."
                    "\nEnter: 1, 2, 3 or q to quit")
