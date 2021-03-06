from handlers.product_handler import get_product
from handlers.customer_handler import get_customer
from utils.quit import quit_loop

def invoice_creation():
    """Enter invoice creation loop"""
    menu = input("\t\tEnter (1). Create invoice or (q). Quit:\n")
    return menu

def product_interface_for_invoice():
    """Selecting products for the invoice"""
    product_table_for_invoice = product_selection_for_invoice()
    return product_table_for_invoice

def customer_interface_for_invoice():
    """Selecting customer for the invoice"""
    customer_list_for_invoice = customer_selection_for_invoice()
    return customer_list_for_invoice

def product_selection_for_invoice():
    """Product creation loop for invoice"""
    product_list = []
    while True:
        enter_product = input("""\t\tEnter: product name
                              \n\t\tOr
                              \n\t\tEnter: quit to go to customer entry\n""")
        if quit_loop(enter_product):
            break
        enter_quantity= input("""\t\tEnter: product quantity
                              \n\t\tOr
                              \n\t\tEnter: quit\n""")
        #Verify quantity type
        try:
            int(enter_quantity)
        except ValueError:
            print("You need to enter an integer")
            continue

        if quit_loop(enter_quantity):
            break

        #Sqlalchemy gets product and calculates quantity and total
        product_for_list = get_product(enter_product)
        quantity_for_list = int(enter_quantity)
        total_for_list = quantity_for_list * int(product_for_list[2])
        product_for_list.append(str(quantity_for_list))
        product_for_list.append(str(total_for_list))
        product_list.append(product_for_list)
    #Verify user entered product and quantity
    if enter_product and enter_quantity:
        column_names = ["Serial", "Description", "Price", "Quantity", "Total price"]
        product_list.append(column_names)
        return product_list
    return None

def customer_selection_for_invoice():
    """Customer selection for invoice"""
    enter_customer = input("""\t\tEnter: customer name
                           \n\t\tOr
                           \n\t\tEnter: quit:\n""")
    if quit_loop(enter_customer):
        return None
    customer_list = get_customer(enter_customer)
    return customer_list
