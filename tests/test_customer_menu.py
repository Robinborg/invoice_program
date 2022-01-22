if __name__ == "__main__" and __package__ is None:
    import sys
    from os import path
    var = path.dirname(path.abspath(__file__)) + "/../src"
    sys.path.append(var)

import interface.customer_interface
from unittest.mock import patch
import unittest

class Test(unittest.TestCase):
    """Test input for menus"""
    @patch("interface.product_interface._get_input", side_effect = ['1', '2', '3', '4'])
    def test_correct_integers(self, input):
        """Test all correct input values"""
        self.assertTrue(interface.customer_interface._customer_menu() == '1' and
                        interface.customer_interface._customer_menu() == '2' and
                        interface.customer_interface._customer_menu() == '3' and
                        interface.customer_interface._customer_menu() == '4')

    @patch("interface.product_interface._get_input", side_effect = ['-1', '-2', '-3', '-4'])
    def test_answer_negative_integers(self, input):
        """Test all negative input values"""
        self.assertFalse(interface.customer_interface._customer_menu() == '1' and
                        interface.customer_interface._customer_menu() == '2' and
                        interface.customer_interface._customer_menu() == '3' and
                        interface.customer_interface._customer_menu() == '4')

    @patch("interface.product_interface._get_input", side_effect = ['11', '22', '33', '44'])
    def test_answer_double_integers(self, input):
        """Test all double integer inputs"""
        self.assertFalse(interface.customer_interface._customer_menu() == '1' and
                        interface.customer_interface._customer_menu() == '2' and
                        interface.customer_interface._customer_menu() == '3' and
                        interface.customer_interface._customer_menu() == '4')

    @patch("interface.product_interface._get_input", side_effect = ['q', 'quit', 'Quit', 'QUIT'])
    def test_answer_correct_quit(self, input):
        """Test all correct inputs of quitting"""
        self.assertTrue(interface.customer_interface._customer_menu() == 'q' and
                        interface.customer_interface._customer_menu() == 'quit' and
                        interface.customer_interface._customer_menu() == 'Quit' and
                        interface.customer_interface._customer_menu() == 'QUIT')

    @patch("interface.product_interface._get_input", side_effect = ['qq', 'qquit', 'QQuit', 'QQUIT'])
    def test_answer_double_string_quit(self, input):
        """Test double entry quitting"""
        self.assertTrue(interface.customer_interface._customer_menu() == 'qq' and
                        interface.customer_interface._customer_menu() == 'qquit' and
                        interface.customer_interface._customer_menu() == 'QQuit' and
                        interface.customer_interface._customer_menu() == 'QQUIT')

    @patch("interface.product_interface._get_input", side_effect = ['pq', 'nquit', 'SQuit', 'TQUIT'])
    def test_answer_leading_wrong_char_quit(self, input):
        """Test misspelling quit"""
        self.assertFalse(interface.customer_interface._customer_menu() == 'q' and
                        interface.customer_interface._customer_menu() == 'quit' and
                        interface.customer_interface._customer_menu() == 'Quit' and
                        interface.customer_interface._customer_menu() == 'QUIT')

    @patch("interface.product_interface._get_input", side_effect = ['    q', '       quit', '       Quit', '      QUIT'])
    def test_answer_leading_whitespace_quit(self, input):
        """Adding extra space to quitting"""
        self.assertFalse(interface.customer_interface._customer_menu() == 'q' and
                        interface.customer_interface._customer_menu() == 'quit' and
                        interface.customer_interface._customer_menu() == 'Quit' and
                        interface.customer_interface._customer_menu() == 'QUIT')


if __name__ == "__main__":
    unittest.main()
