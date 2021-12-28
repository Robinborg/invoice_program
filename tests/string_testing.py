from unittest import mock
from unittest import TestCase

from invoice_program.interface.customer_interface import _customer_menu




class TestInputString(TestCase):

    @mock.patch("_customer_menu.input", side_effect = ['1', '-1', '2', '-2', '3', '-3', '4', '-4', 'q', 'Q'])
    def test_input_string_one(self, _customer_menu):
        calling_1 = _customer_menu()
        calling_m1 = _customer_menu()
        calling_2 = _customer_menu()
        calling_m2 = _customer_menu()
        calling_3 = _customer_menu()
        calling_m3 = _customer_menu()
        calling_4 = _customer_menu()
        calling_m4 = _customer_menu()
        calling_q = _customer_menu()
        calling_Q = _customer_menu()
        self.assertTrue(calling_1 == '1' and
                        calling_2 == '2' and
                        calling_3 == '3' and
                        calling_4 == '4' and
                        calling_q == 'q')

if __name__ == "__main__":
    TestInputString()


#For management loop: mocked_input.side_effect = ['-1', '1', '-2', '2','-3', '3','-4', '4', 'q', 'Q']
