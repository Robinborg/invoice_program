from handlers.product_handler import get_product
from typing import List

def invoice_creation():
    menu = input("\t\tEnter (1). Create invoice or (q). Quit:\n")
    return menu

def interface():
    product_table_for_invoice = product_selection_for_invoice()
    return product_table_for_invoice

def product_selection_for_invoice():
    product_list = []
    quantity = 0
    while True:
        create_mode = input("\t\t(1). To enter product (q). Quit\n")
        if create_mode == 'q':
            break
        else:
            enter_product = input("\t\tEnter product name:\n")
            enter_quantity= input("\t\tEnter product quantity:\n")
            if enter_product == 'q':
                break
            product_for_list = get_product(enter_product)
            print(product_for_list)
            quantity_for_list = int(enter_quantity)
            print(quantity_for_list)
            print(product_for_list[2])
            total_for_list = quantity_for_list * int(product_for_list[2])
            product_list.append(product_for_list)
            product_list[0].append(str(quantity_for_list))
            product_list[0].append(str(total_for_list))
    column_names = ["Serial", "Description", "Price", "Quantity", "Total price"]
    product_list.append(column_names)
    return product_list
