from invoice_template import InvoiceTemplate
from models import Customer, Product, ProductsInvoice, Invoice
from interface.invoice_creation_interface import customer_interface_for_invoice, product_interface_for_invoice
from handlers.invoice_handler import get_invoice_serial, add_invoice





def create_invoice_help()->bool:
    # Fetch products from database for invoice
    products_list = product_interface_for_invoice()
    # Fetch customer from databse for invoice
    customer_list = customer_interface_for_invoice()
    # Break out of invoice creation if None is returned customer_list or product_list
    if customer_list is None or len(products_list) <= 1:
        return False
    # Fill customer for database
    customer_to_invoice_relationship = Customer(
                          name = customer_list[0],
                          address = customer_list[1],
                          phone = customer_list[2])
    # list of products for ProductsInvoice
    full_list_of_products_invoices = []
    # Iterate produts_list to append full_list_of_products for ProductsInvoice
    for product_row in range(0, len(products_list) - 1):
        # Fill product for database
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

    print(full_list_of_products_invoices)
    # Get latest invoice number and add one for the new invoice
    # If there is no prior set the number to 10000
    invoice_serial = get_invoice_serial() + 1

    # Fill invoice for database
    invoice_to_database = Invoice(serial = invoice_serial,
                        customer_relationship = customer_to_invoice_relationship,
                        products_invoice_relationship = full_list_of_products_invoices)

    # Add invoice to database
    add_invoice(invoice_to_database)

    # Create the invoice PDF
    make_invoice = InvoiceTemplate(str(invoice_serial))
    if len(products_list) > 8:
        help_slice = 0
        for eight in range(8, len(products_list), 8):
            if eight < 8:
                make_invoice.make_data_table(products_list[help_slice:])
                make_invoice.create_document(invoice_number = eight,
                                             customer_name = customer_list[0],
                                             customer_address = customer_list[1],
                                             customer_phone = customer_list[2])
            else:
                make_invoice.make_data_table(products_list[help_slice:eight])
                make_invoice.create_document(invoice_number = eight,
                                             customer_name = customer_list[0],
                                             customer_address = customer_list[1],
                                             customer_phone = customer_list[2])
            help_slice += 8
    else:
        make_invoice.make_data_table(products_list)
        make_invoice.create_document(invoice_number = invoice_serial,
                                     customer_name = customer_list[0],
                                     customer_address = customer_list[1],
                                     customer_phone = customer_list[2])
        make_invoice.show_page()
    make_invoice.save_pdf()
    return True
