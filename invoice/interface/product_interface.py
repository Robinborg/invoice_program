from handlers.product_handler import add_product, all_products, remove_product, show_product, get_product
from models.product import Product
from utils.quit import quit_loop

def _get_input(text:str)->str:
    return input(text)

def _product_menu()->str:
    """Display options for product mode"""
    product_menu = _get_input("\t\tChoose from the options:\n\t\t"
                         "(1). Enter a new product\n\t\t"
                         "(2). Display all products\n\t\t"
                         "(3). Display a product\n\t\t"
                         "(4). Delete a product\n\t\t"
                         "(q). quit\n")
    return product_menu

def product_management_loop():
    """Product management for database"""
    while True:
        chosen_menu = _product_menu()
        if quit_loop(chosen_menu):
            break
        elif chosen_menu == '1':
            product_serial = input("\t\tEnter product serial\n")
            product_description = input("\t\tEnter product description\n")
            product_price = input("\t\tEnter product price\n")
            product_details= Product(serial=product_serial,
                                  description=product_description,
                                  price=product_price)
            add_product(product_details)
        elif chosen_menu == '2':
            all_products()
        elif chosen_menu == '3':
            product_description = input("\t\tSearch for a product by description\n")
            show_product(product_description)
        elif chosen_menu == '4':
            product_description = input("\t\tRemove a product by description\n")
            remove_product(product_description)
        else:
            print("You did not enter q, 1, 2, 3 or 4")

