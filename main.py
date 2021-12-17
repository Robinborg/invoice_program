'''Generate invoices'''
from invoice_template import InvoiceTemplate
from interface.invoice_interface import product_interface_for_invoice, \
                                        customer_interface_for_invoice
from interface.product_interface import product_management_loop
from interface.customer_interface import customer_management_loop
from handlers import invoice_handler
from models import *

if __name__ == "__main__":
    while True:
        enter_mode = input("\t\tEnter:\n\t\t"
                            "(1). Product mode\n\t\t"
                            "(2). Customer mode\n\t\t"
                            "(3). Make invoice\n\t\t"
                            "(q). Quit\n")
        if enter_mode == '1':
            product_management_loop()
        elif enter_mode == '2':
            customer_management_loop()
        elif enter_mode == '3':
            products_list = product_interface_for_invoice()
            customer_list = customer_interface_for_invoice()

            product_1 = Product(serial = products_list[0][0],
                                description = products_list[0][1],
                                price = products_list[0][2])
         
            customer_1 = Customer(name = customer_list[0],
                                  address = customer_list[1],
                                  phone = customer_list[2])
            #TODO: Make it possibe to iterate the products_list to add all products_lists to database 
            products_invoice_1 = ProductsInvoice(product_relationship = product_1,
                                                 product_serial = products_list[0][0],
                                                 product_description = products_list[0][1],
                                                 product_rate = products_list[0][2],
                                                 product_quantity = products_list[0][3],
                                                 product_total = products_list[0][4] 
                                                 )
         
            invoice_1 = Invoice(customer_relationship = customer_1,
                                products_invoice_relationship = [products_invoice_1])
            invoice_handler.add_invoice(invoice_1)


            #TODO:Retrieve latest invoice number to add to InvoiceTemplate("latest_number+1")
            make_invoice = InvoiceTemplate("100")
            make_invoice.make_data_table(products_list)
            make_invoice.create_document(invoice_number = 0,
                                           customer_name = customer_list[0],
                                           customer_address = customer_list[1],
                                           customer_phone=customer_list[2])
            make_invoice.save_pdf()
        elif enter_mode == 'q':
            break
        else:
            print("You did not enter the right mode."
                    "\nEnter: 1, 2, 3 or q to quit")
