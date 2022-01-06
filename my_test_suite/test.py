if __name__ == "__main__" and __package__ is not None:
    import sys
    from os import path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    import customer_interface._customer_menu

from unittest import TestCase
from unittest import mock
import unittest

class TestInput(TestCase):
    """Test input for menus"""
    @mock.patch("_customer_menu.input", side_effect=['1', '2', '3', '4', 'q'])
    def test_customer_menu(self, _customer_menu):
        """Testing customer_menu"""
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


#    @mock.patch("_product_menu.input", side_effect=['1', '2', '3', '4', 'q'])
#    def test_product_menu(self, _customer_menu):
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
