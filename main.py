'''Generate invoices'''

from invoice import InvoiceTemplate
from database_tools.handling_data import DataHandler
from models.customer import Customer
from models.product import Product
import sys

#Make default number
if __name__ == "__main__":
"""
Displays to the user options for the commands
1. Enter a new product
2. Display a product
3. Display all products
3. Modify a product
4. Delete a product
"""
"""User enters command 

Program checks it's a valid command
  Wrong input: error and reprint the options
  Right input: ->

Enter new product: 
    Displays the sample of a product entry
    For each product field:
        prompt user for field
        if it's wrong: reprompt
        if it's right: next field
    user can confirm
"""




















































#    first_invoice = InvoiceTemplate("2")
#    modify_data = DataHandler()
#    make_table = modify_data.creating_table(select_index=1, quantity=2)
#    #print(make_table)
#    first_invoice.make_data_table(make_table)
#    #modify_data.removing_row(delete_all=False)
#    #modify_data.adding_customer_details("George", "Starbase", 9999)
#    #modify_data.adding_product_details(serial=100, description="Hammer", rate=15)
#    #modify_data.show_table()
#    customer_details = modify_data.working_customer_info(1)
#    first_invoice.create_document(invoice_number=2,
#            customer_name = customer_details[0], customer_phone = customer_details[2])
#    first_invoice.save_pdf()
#    while True:
#        enter_command = input("Enter instruction: ")
#        if enter_command.lower() == 'quit':
#            break
#        elif enter_command.lower() == "add product":
#            add_product_serial= input("Enter product serial: ")
#            add_product_goods_description = input("Enter product goods and description: ")
#            add_product_rate= input("Enter product rate: ")
#            modify_data.adding_product_details(add_product_serial,
#                    add_product_goods_description, add_product_rate)
#            continue
#        elif enter_command.lower() == 'add customer':
#            add_customer_name = input("Enter customer name: ")
#            add_customer_address = input("Enter customer address: ")
#            add_customer_phone = input("Enter customer phone: ")
#            modify_data.adding_customer_details(add_customer_name, add_customer_address,
#                    add_customer_phone)
#            continue
#
