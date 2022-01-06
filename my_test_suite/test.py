#if __name__ == "__main__" and __package__ is None:
#    from sys import path
#    from os.path import dirname
#    path.append(dirname(path[0]))
#    __package__ = "examples"
#
if __name__ == "__main__" and __package__ is None:
    import sys
    from os import path
    var = path.dirname(path.abspath(__file__)) + "/../src"
    print("-"*60)
    print(var)
    print("-"*60)
    sys.path.append(var)
    print(sys.path)
    print("-"*60)

import interface.customer_interface
from unittest import TestCase
from unittest import mock
import unittest

class TestInput(TestCase):
    """Test input for menus"""
    @mock.patch("interface.customer_interface._customer_menu.customer_mode", side_effect=['1', '2', '3', '4', 'q'])
    def test_customer(self, customer_menu):
        """Testing customer_menu"""
        calling_1 = interface.customer_interface._customer_menu()
        calling_2 = interface.customer_interface._customer_menu()
        calling_3 = interface.customer_interface._customer_menu()
        calling_4 = interface.customer_interface._customer_menu()
        calling_q = interface.customer_interface._customer_menu()
        self.assertTrue(calling_1 == '1' and
                        calling_2 == '2' and
                        calling_3 == '3' and
                        calling_4 == '4' and
                        calling_q == 'q')


#    @mock.patch("_product_menu.input", side_effect=['1', '2', '3', '4', 'q'])
#    def test_product_menu(self, ci._customer_menu):
#        """Testing product menu"""
#        calling_1 = _product_menu()
#        calling_2 = _product_menu()
#        calling_3 = _product_menu()
#        calling_4 = _product_menu()
#        calling_q = _product_menu()
#        self.assertTrue(calling_1 == '1' and
#                        calling_2 == '2' and
#                        calling_3 == '3' and
#                        calling_4 == '4' and
#                        calling_q == 'q')
#
if __name__ == "__main__":
    unittest.main()
