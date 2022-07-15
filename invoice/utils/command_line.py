from invoice_template import InvoiceTemplate

def model_invoice():
    """Make a model invoice in pdf_invoices folder"""
    make_model_invoice = InvoiceTemplate("101010")
    make_model_invoice.make_data_table([["7829",
                                         "Computer",
                                         "1200",
                                         "1",
                                         "1200"],
                                        ["Serial",
                                         "Goods and Description",
                                         "Rate",
                                         "Quantity",
                                         "Total"]])
    make_model_invoice.create_document(invoice_number = "101010",
                                       customer_name = "Joe Sample",
                                       customer_address = "Main street",
                                       customer_phone = "555-555")
    make_model_invoice.save_pdf()
