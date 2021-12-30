import sys

sys.path.append("Users/coalchewer/src/code/RobinBorg/python/invoice_program/interface")

from interface.customer_interface import _customer_menu
from unittest import TestCase
from unittest import mock
import unittest

class TestInput(TestCase):

    @mock.patch("_customer_menu.input", side_effect=['1', '2', '3', '4', 'q'])
    def test_customer_menu(self, _customer_menu):
        calling_1 = _customer_menu()
        calling_2 = _customer_menu()
        calling_3 = _customer_menu()
        calling_4 = _customer_menu()
        calling_q = _customer_menu()
        self.assertTrue(calling_1 == '1' and
                        calling_2 == '2' and
                        calling_3 == '3' and
                        calling_4 == '4' and
                        calling_q == 'q')
        self.assertTrue(calling_1 == '20')


if __name__ == "__main__":
    unittest.main()
