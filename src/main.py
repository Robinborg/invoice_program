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
import argparse
from invoice_template import InvoiceTemplate

def main():
    #Command line argument for printing an invoice
    parser = argparse.ArgumentParser()
    parser.add_argument("--invoice",
                        action = "store_true")
    args = parser.parse_args()
    make_model_invoice = InvoiceTemplate("101010")
    make_model_invoice.make_data_table([["7829",
                                         "Computer",
                                         "1299",
                                         "1",
                                         "1299"],
                                        ["Serial",
                                        "Goods and description",
                                        "Rate",
                                        "Quantity",
                                        "Total"]])
    make_model_invoice.create_document(invoice_number = "101010",
                                       customer_name = "Joe Doe",
                                       customer_address = "Main street",
                                       customer_phone = "9999999")
    make_model_invoice.save_pdf()
    if args.invoice:
        return "You got an invoice in pdf_invoices folder"
    #Main event loop for the program
    while True:
        enter_mode = input("\t\tEnter:\n\t\t"
                            "(1). Product mode\n\t\t"
                            "(2). Customer mode\n\t\t"
                            "(3). Invoice mode\n\t\t"
                            "(4). Make an invoice\n\t\t"
                            "(q). Quit\n")
        if enter_mode == '1':
            product_management_loop()

        elif enter_mode == '2':
            customer_management_loop()

        elif enter_mode == '3':
            invoice_management_loop()

        elif enter_mode == '4':
            #Fetch products from database for invoice
            products_list = product_interface_for_invoice()
            #Fetch customer from databse for invoice
            customer_list = customer_interface_for_invoice()
            #Break out of invoice creation if None is returned customer_list | product_list
            if customer_list is None or len(products_list) <= 1:
                break
            #Fill customer for database
            customer_to_invoice_relationship = Customer(
                                  name = customer_list[0],
                                  address = customer_list[1],
                                  phone = customer_list[2])
            #Full list of products for ProductsInvoice
            full_list_of_products_invoices = []
            #Iterate produts_list to append full_list_of_products for ProductsInvoice
            for product_row in range(0, len(products_list) - 2):
                #Fill product for database
                product_to_products_invoice_relationship = Product(
                                    serial = products_list[product_row][0],
                                    description = products_list[product_row][1],
                                    price = products_list[product_row][2])
                products_invoice_list = ProductsInvoice(
                                        product_relationship = product_to_products_invoice_relationship,
                                        product_serial = products_list[product_row][0],
                                        product_description = products_list[product_row][1],
                                        product_rate = products_list[product_row][2],
                                        product_quantity = products_list[product_row][3],
                                        product_total = products_list[product_row][4])
                full_list_of_products_invoices.append(products_invoice_list)
            #Get latest invoice number and add one for the new invoice
            #If there is no prior set the number to 10000
            if get_invoice_serial() == None or get_invoice_serial() == 0:
                invoice_serial = 10000
            else:
                invoice_serial = get_invoice_serial() + 1
            #Fill invoice for database
            invoice_to_database = Invoice(serial = invoice_serial,
                                customer_relationship = customer_to_invoice_relationship,
                                products_invoice_relationship = full_list_of_products_invoices)
            #Add invoice to database
            add_invoice(invoice_to_database)

            #Create the invoice PDF
            make_invoice = InvoiceTemplate(str(invoice_serial))
            if 32 >= len(products_list) >= 16:
                make_invoice.make_data_table(products_list[:8])
                make_invoice.create_document(invoice_number = invoice_serial,
                                           customer_name = customer_list[0],
                                           customer_address = customer_list[1],
                                           customer_phone=customer_list[2])
                make_invoice.show_page()
                make_invoice.make_data_table(products_list[8:16])
                make_invoice.create_document(invoice_number = invoice_serial,
                                           customer_name = customer_list[0],
                                           customer_address = customer_list[1],
                                           customer_phone=customer_list[2])
                make_invoice.show_page()
                make_invoice.make_data_table(products_list[16:32])
                make_invoice.create_document(invoice_number = invoice_serial,
                                           customer_name = customer_list[0],
                                           customer_address = customer_list[1],
                                           customer_phone=customer_list[2])
                make_invoice.show_page()
            if 16 >= len(products_list) >= 8:
                make_invoice.make_data_table(products_list[:8])
                make_invoice.create_document(invoice_number = invoice_serial,
                                           customer_name = customer_list[0],
                                           customer_address = customer_list[1],
                                           customer_phone=customer_list[2])
                make_invoice.make_data_table(products_list[8:16])
                make_invoice.create_document(invoice_number = invoice_serial,
                                           customer_name = customer_list[0],
                                           customer_address = customer_list[1],
                                           customer_phone=customer_list[2])
                make_invoice.show_page()
            if len(products_list) < 10:
                make_invoice.make_data_table(products_list)
                make_invoice.create_document(invoice_number = invoice_serial,
                                           customer_name = customer_list[0],
                                           customer_address = customer_list[1],
                                           customer_phone=customer_list[2])
                make_invoice.make_data_table(products_list)
            make_invoice.save_pdf()
        elif quit_loop(enter_mode):
            break
        else:
            print("You did not enter the right mode."
                    "\nEnter: 1, 2, 3 or q to quit")

if __name__ == "__main__":
    main()
