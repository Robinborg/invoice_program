'''Generate invoices'''

#from invoice import InvoiceTemplate
#from database_tools.handling_data import DataHandler
#import sys
from utils.mode_message import choose_mode
from utils.product_messages import product_menu, enter_product, display_all_products, display_product, modify_product
from utils.customer_messages import customer_menu, enter_customer, display_all_customers, display_customer, modify_customer, delete_customer
from utils.invoice_messages import invoice_menu
from handlers.customer_handler import adding_customer, all_customers, removing_customer, show_customer

from models.customer import Customer

if __name__ == "__main__":
    #choose_mode()
    #adding_customer(Customer(first_name='bob', last_name='Bird',\
    #    address='Coockoo', phone='44444444'))
    all_customers()
    #removing_customer(delete_customer='Jay')
    #show_customer('Jay')
    #prin("New")
    #show_customer()
    #testing()

    #product_menu()
    #enter_product()
    #display_all_products()
    #display_product()
    #modify_product()
    #customer_menu()
    #enter_customer()
    #display_all_customers()
    #display_customer()
    #modify_customer()
    #delete_customer()
    #invoice_menu()

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

1.Enter new product: 
    Displays the sample of a product entry
    For each product field:
        prompt user for field
        if it's wrong: reprompt
        elif it's right: next field
    user confirms addition
2. Display a product
    Displays options for searching a product
        - by name
        - by index
    prompt user for input
        if it's wrong: reprompt
        elif right: show product the user requested
3. Display all products
    Display command for showing all products
    prompt user for input
        if wrong: reprompt
        elif right: show all products
4. delete a product
    Display command for deleting a product
    prompt user for input:
        if wrong: reprompt
        elif right: ask user to verify deletion
    user verifies deletion.
"""





















































#    first_invoice = InvoiceTemplate("2")
#    modify_data = DataHandler()
#    make_table = modify_data.creating_table(select_index=1, quantity=2)
#    print(make_table)
#    first_invoice.make_data_table(make_table)
#    modify_data.removing_row(delete_all=False)
#    modify_data.adding_customer_details("George", "Starbase", 9999)
#    modify_data.adding_product_details(serial=100, description="Hammer", rate=15)
#    modify_data.show_table()
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
