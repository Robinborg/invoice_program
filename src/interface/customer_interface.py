"""Collection of messages for customer mode"""
from handlers.customer_handler import add_customer, all_customers, remove_customer, show_customer, get_customer
from models.customer import Customer
from utils.quit import quit_loop

def _get_input(text):
    return input(text)

def _customer_menu():
    """Display options for customer mode"""
    customer_mode = _get_input("\t\tChoose from the options:\n\t\t"
                          "(1). Enter a new customer\n\t\t"
                          "(2). Display all customers\n\t\t"
                          "(3). Display a customers\n\t\t"
                          "(4). Delete a customer\n\t\t"
                          "(q). Quit\n")
    return customer_mode

def customer_management_loop():
    """Customer handling for database"""
    while True:
        chosen_menu = _customer_menu()
        if quit_loop(chosen_menu):
            break
        elif chosen_menu == '1':
            customer_name= input("\t\tEnter customer name\n")
            customer_address = input("\t\tEnter customer address\n")
            customer_phone = input("\t\tEnter customer phone\n")
            customer_details = Customer(name=customer_name,
                                        address=customer_address,
                                        phone=customer_phone)
            add_customer(customer_details)
        elif chosen_menu == '2':
            all_customers()
        elif chosen_menu == '3':
            customer_name= input("\t\tSearch for a customer by name\n")
            show_customer(customer_name)
        elif chosen_menu == '4':
            customer_name = input("\t\tRemove a customer by name\n")
            remove_customer(customer_name)
        else:
            print("You did not ener 1, 2, 3 or 4")
