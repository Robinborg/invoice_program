from handlers.product_handler import get_product
from typing import List

def invoice_creation():
    menu = input("\t\tEnter (1). Create invoice or (q). Quit:\n")
    return menu


def interface() -> List[str]:
    product_list = []
    quantity = 0
    while True:
        create_mode = input("\t\t(1). To enter product (q). Quit\n")
        if create_mode == 'q':
            break
        else:
            enter_product = input("\t\tEnter product name:\n")
            if enter_product == 'q':
                break
            add_to_list = get_product(enter_product)
            print(add_to_list)
            if add_to_list in product_list:
                quantity += 1
            else:
                product_list.append(add_to_list)
    return product_list
