if __name__ == "__main__" and __package__ is None:
    import sys
    from os import path
    var = path.dirname(path.abspath(__file__)) + "/../invoice"
    sys.path.append(var)

import interface.invoice_interface
from unittest.mock import patch
import unittest

class Test(unittest.TestCase):
    """Test input for menus"""
    @patch("interface.invoice_interface._get_input", return_value = '1')
    def test_answer_one(self, input):
        self.assertEqual(interface.invoice_interface._invoice_menu(), '1')

    @patch("interface.invoice_interface._get_input", return_value = '2')
    def test_answer_two(self, input):
        self.assertEqual(interface.invoice_interface._invoice_menu(), '2')

    @patch("interface.invoice_interface._get_input", return_value = '3')
    def test_answer_three(self, input):
        self.assertEqual(interface.invoice_interface._invoice_menu(), '3')

    @patch("interface.invoice_interface._get_input", return_value = '4')
    def test_answer_four(self, input):
        self.assertEqual(interface.invoice_interface._invoice_menu(), '4')

    @patch("interface.invoice_interface._get_input", return_value = 'q')
    def test_answer_quit(self, input):
        self.assertEqual(interface.invoice_interface._invoice_menu(), 'q')

    @patch("interface.invoice_interface._get_input", return_value = 'quit')
    def test_answer_quit_two(self, input):
        self.assertEqual(interface.invoice_interface._invoice_menu(), 'quit')

    @patch("interface.invoice_interface._get_input", return_value = 'Quit')
    def test_answer_quit_three(self, input):
        self.assertEqual(interface.invoice_interface._invoice_menu(), 'Quit')
if __name__ == "__main__":
    unittest.main()
