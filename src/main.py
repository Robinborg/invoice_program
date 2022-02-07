"""Manage database and create invoice pdfs"""
from invoice_template import InvoiceTemplate
from interface.product_interface import product_management_loop
from interface.customer_interface import customer_management_loop
from interface.invoice_interface import invoice_management_loop
from utils.quit import quit_loop
import argparse
from utils.command_line import model_invoice
from utils.invoice_create_helper import create_invoice_help

def main():
    #Command line argument for printing an invoice
    parser = argparse.ArgumentParser()
    parser.add_argument("-sample-invoice",
                        action = "store_true")
    args = parser.parse_args()
    if args.sample_invoice:
        model_invoice()
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
            create_invoice_help()

        elif quit_loop(enter_mode):
            break

        else:
            print("You did not enter the right mode."
                    "\nEnter: 1, 2, 3 or q to quit")

if __name__ == "__main__":
    main()
