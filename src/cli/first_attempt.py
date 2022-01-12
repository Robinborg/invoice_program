import sys
sys.path.append("/Users/coalchewer/code/python/invoice_program/src")
from invoice_template import InvoiceTemplate
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-invoice',
                    action = "store_true")
args = parser.parse_args()

if len(sys.argv) <= 1:
    sys.argv.append("--help")

if args.invoice:
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
                                       customer_phone = "4983820")
    make_model_invoice.save_pdf()
else:
    print("jumped the function")

