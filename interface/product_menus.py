"""Collection of messages for product mode"""
from collections import Counter
from typing import List
from handlers.product_handler import adding_product, all_products, removing_product, show_product, get_product
from models.product import Product

def _product_menu():
    """Display options for product mode"""
    product_menu = input("\t\tChoose from the options:\n\t\t(1). Enter a new product\n\t\t(2). Display all products\n\t\t(3). Display a product\n\t\t(4). Delete a product\n\t\t(q). quit\n")
    return product_menu

def calculate_quantity(nums: List[str]) -> int:
    """Quantity of products in list"""
    how_many = Counter(nums)
    print(how_many)
    return how_many

def product_event_loop():
    while True:
        chosen_menu = _product_menu()
        if chosen_menu == 'q':
            break
        elif chosen_menu == '1':
            product_serial = input("\t\tEnter product serial\n")
            product_description = input("\t\tEnter product description\n")
            product_price = input("\t\tEnter product price\n")
            new_product = Product(serial=product_serial, description=product_description, price=product_price)
            adding_product(new_product)
        elif chosen_menu == '2':
            all_products()
        elif chosen_menu == '3':
            search_product = input("\t\tSearch for a product by description\n")
            show_product(search_product)
        elif chosen_menu == '4':
            remove_product = input("\t\tRemove a product by description\n")
            removing_product(remove_product)
        else:
            print("You did not ener 1, 2, 3 or 4")

