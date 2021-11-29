'''Generate invoices'''

import itertools
from invoice import InvoiceTemplate
#from database_tools.handling_data import DataHandler
from interface.product_menus import product_menu, calculate_quantity
from interface.customer_menus import customer_menu
from interface.invoice_menus import interface
from utils.create_table import adding_products
from handlers.product_handler import adding_product, all_products, removing_product, show_product, get_product
from handlers.customer_handler import adding_customer, all_customers, removing_customer, show_customer
from models.customer import Customer
from models.product import Product


if __name__ == "__main__":
    choosing_mode = input("\t\tEnter:\n\t\t(1). Product mode\n\t\t"\
            "(2). Customer mode\n\t\t(3). Make invoice\n\t\t(q). Quit\n")
    if choosing_mode == '1':
        while True:
            chosen_menu = product_menu()
            if chosen_menu == 'q':
                break
            elif chosen_menu == '1':
                product_serial = input("\t\tEnter product serial\n")
                product_description = input("\t\tEnter product description\n")
                product_price = input("\t\tEnter product price\n")
                new_product = Product(serial = product_serial, description=product_description,\
                        price=product_price)
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


    elif choosing_mode == '2':
        while True:
            chosen_menu = customer_menu()
            if chosen_menu == 'q':
                break
            elif chosen_menu == '1':
                customer_name= input("\t\tEnter customer name\n")
                customer_address = input("\t\tEnter customer address\n")
                customer_phone = input("\t\tEnter customer phone\n")
                new_customer = Customer(name=customer_name, address=customer_address,\
                        phone=customer_phone)
                adding_customer(new_customer)
            elif chosen_menu == '2':
                all_customers()
            elif chosen_menu == '3':
                search_customer = input("\t\tSearch for a customer by name\n")
                show_product(search_customer)
            elif chosen_menu == '4':
                remove_customer = input("\t\tRemove a customer by name\n")
                removing_customer(remove_customer)
            else:
                print("You did not ener 1, 2, 3 or 4")

    elif choosing_mode == '3':
        products = interface()
        #flatten 1 from List[List[Tuple[str]]
        flatten_products = itertools.chain.from_iterable(products)
        #Testing
        listing = [list(num) for num in flatten_products]
        #flatten 2 from List[Tuple[str]]
        #flatten_2 = [item for sublist in flatten_products for item in sublist]
        #Calculate quantity
        #calc = calculate_quantity(flatten_2)
        #make into List[List[str]]
        #nested_list = [flatten_2]
        #print(nested_list)

        #Make quantity function to calculate apperance in flatten_2

        making_invoice = InvoiceTemplate("100")
        making_invoice.make_data_table(listing)
        making_invoice.create_document(100, "Clark", 9876)
        making_invoice.save_pdf()

    elif choosing_mode == 'q':
        pass
    else:
        print("You did not enter the right mode. Rerun the program and choose 1, 2, 3 or q to quit")






















































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
