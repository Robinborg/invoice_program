"""Collection of messages for customer mode"""

def customer_menu():
    """Display options for customer mode"""
    customer_mode = input("\t\tChoose from the options:\n\t\t(1). Enter a new customer\n\t\t(2). Display all customers\n\t\t(3). Display all customers \n\t\t(4). Delete a customer\n\t\t(q). Quit\n")
    return customer_mode

def enter_customer():
    """Shows how to enter a new customer"""
    print("\n")
    print("\t\tEnter new customer: [ID], [First name], [Last name], [Address], [Phone]\n")
    print("\t\tEnter: \n")

def display_all_customers():
    """Command to show all customers"""
    print("\n")
    print("\t\tDisplay all customers:\n")
    print("\t\tEnter: (1) \n")
    print("\t\t(Q|quit) to exit")

def display_customer():
    """Shows how to display a customer"""
    print("\n")
    print("\t\tDisplay a customer:\n")
    print("\t\tEnter: \n")
    print("\t\t(1). ID\n")
    print("\t\t(2). Name\n")
    print("\t\t(Q|quit) to exit")

def modify_customer():
    """Shows how to modify a customer"""
    print("\n")
    print("\t\tModify a customer\n")
    print("\t\tEnter: \n")
    print("\t\t(1). ID\n")
    print("\t\t(2). Name\n")
    print("\t\t(Q|quit) to exit")

def delete_customer():
    """Shows how to modify a customer"""
    print("\n")
    print("\t\tDelete a customer\n")
    print("\t\tEnter: \n")
    print("\t\t(1). ID\n")
    print("\t\t(2). Name\n")
    print("\t\t(Q|quit) to exit")
