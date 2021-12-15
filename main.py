'''Generate invoices'''
from invoice import InvoiceTemplate
from interface.invoice_interface import product_interface_for_invoice, \
                                        customer_interface_for_invoice
from interface.product_interface import product_management_loop
from interface.customer_interface import customer_management_loop

if __name__ == "__main__":
    while True:
        choose_mode = input("\t\tEnter:\n\t\t"
                            " (1). Product mode\n\t\t"
                            " (2). Customer mode\n\t\t"
                            " (3). Make invoice\n\t\t"
                            " (q). Quit\n")
        if choose_mode == '1':
            product_management_loop()
        elif choose_mode == '2':
            customer_management_loop()
        elif choose_mode == '3':
            products_list = product_interface_for_invoice()
            customer_list = customer_interface_for_invoice()
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
                  " Choose 1, 2, 3 or q to quit")

