from handlers.invoice_handler import add_invoice, all_invoices,\
                                     remove_invoice, show_invoice, get_invoice_serial
from utils.quit import quit_loop



def _get_input(text:str)->str:
    return input(text)

def _invoice_menu()->str:
    """Display options for invoice mode"""
    invoice_menu = _get_input("\t\tChoose from the options:\n\t\t"
                         "(1). Display all invoices\n\t\t"
                         "(2). Display an invoice\n\t\t"
                         "(3). Delete an invoice\n\t\t"
                         "(q). Quit\n")
    return invoice_menu

def invoice_management_loop():
    """Invoice management for database"""
    while True:
        chosen_menu = _invoice_menu()
        if quit_loop(chosen_menu):
            break
        elif chosen_menu == '1':
            all_invoices()

        elif chosen_menu == '2':
            invoice_serial = input("\t\tSearch for invoice by serial: \n")
            show_invoice(invoice_serial)
        elif chosen_menu == '3':
            invoice_serial = input("\t\tSearch for invoice by serial: \n")
            remove_invoice(invoice_serial)
        else:
            print("You did not enter q, 1, 2, 3 or 4")
