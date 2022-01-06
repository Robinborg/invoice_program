from typing import List
from handlers.product_handler import show_product


def adding_products():
    list_products = []
    while True:
        choosing = input("Product choosing mode:\n")
        if choosing != 'q':
            product_adding_mode = input("Select a product by name:\n")
            limbo = show_product(product_adding_mode)
            list_products.append(limbo)
        else:
            print("You have exited product choosing mode and your products are in a list")
    return list_products


        

def table_invoice(select_product: List) -> List[List[str]]:
    """Create the table for the invoice template"""
    product_table = [
            select_product,
            ["Serial", "Description", "Rate", "Quantity", "Total"],
            ]
    return product_table

