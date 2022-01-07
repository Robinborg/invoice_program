if __name__ == "__main__" and __package__ is None:
    import sys
    from os import path
    var = path.dirname(path.abspath(__file__)) + "/../src"
    sys.path.append(var)

import interface.customer_interface
from unittest import TestCase
from unittest import mock
import unittest

class TestInput(TestCase):
    """Test input for menus"""
    def test_customer(self):
        """Testing customer_menu"""
        input_values = ['1', '2','3', '4', 'q']
        output = []

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)
        interface.customer_interface.input = mock_input
        interface.customer_interface.print = lambda s: output.append(s)
        interface.customer_interface._customer_menu()

        assert output == ['1','2','3','4','q',]



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
