'''Generate invoices'''

from invoice import InvoiceTemplate

first_invoice = InvoiceTemplate('jane_smith', 1)

first_invoice.blank_canvas()
    
#Need to build the invoice in one go
'''Which means that,
   1. Load data from database
   2. Input client, product
   3. Send information to Canvas
'''

