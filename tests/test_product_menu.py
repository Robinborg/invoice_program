if __name__ == "__main__" and __package__ is None:
    import sys
    from os import path
    var = path.dirname(path.abspath(__file__)) + "/../invoice"
    sys.path.append(var)

import interface.product_interface
from unittest.mock import patch
import unittest

class Test(unittest.TestCase):
    """Test input for menus"""
    @patch("interface.product_interface._get_input", side_effect = ['1', '2', '3', '4'])
    def test_correct_integers(self, input):
        self.assertTrue(interface.product_interface._product_menu() == '1' and
                        interface.product_interface._product_menu() == '2' and
                        interface.product_interface._product_menu() == '3' and
                        interface.product_interface._product_menu() == '4')

    @patch("interface.product_interface._get_input", side_effect = ['-1', '-2', '-3', '-4'])
    def test_answer_negative_integers(self, input):
        self.assertFalse(interface.product_interface._product_menu() == '1' and
                        interface.product_interface._product_menu() == '2' and
                        interface.product_interface._product_menu() == '3' and
                        interface.product_interface._product_menu() == '4')

    @patch("interface.product_interface._get_input", side_effect = ['11', '22', '33', '44'])
    def test_answer_double_integers(self, input):
        self.assertFalse(interface.product_interface._product_menu() == '1' and
                        interface.product_interface._product_menu() == '2' and
                        interface.product_interface._product_menu() == '3' and
                        interface.product_interface._product_menu() == '4')

    @patch("interface.product_interface._get_input", side_effect = ['q', 'quit', 'Quit', 'QUIT'])
    def test_answer_correct_quit(self, input):
        self.assertTrue(interface.product_interface._product_menu() == 'q' and
                        interface.product_interface._product_menu() == 'quit' and
                        interface.product_interface._product_menu() == 'Quit' and
                        interface.product_interface._product_menu() == 'QUIT')

    @patch("interface.product_interface._get_input", side_effect = ['qq', 'qquit', 'QQuit', 'QQUIT'])
    def test_answer_double_string_quit(self, input):
        self.assertTrue(interface.product_interface._product_menu() == 'qq' and
                        interface.product_interface._product_menu() == 'qquit' and
                        interface.product_interface._product_menu() == 'QQuit' and
                        interface.product_interface._product_menu() == 'QQUIT')

    @patch("interface.product_interface._get_input", side_effect = ['pq', 'nquit', 'SQuit', 'TQUIT'])
    def test_answer_leading_wrong_char_quit(self, input):
        self.assertFalse(interface.product_interface._product_menu() == 'q' and
                        interface.product_interface._product_menu() == 'quit' and
                        interface.product_interface._product_menu() == 'Quit' and
                        interface.product_interface._product_menu() == 'QUIT')

    @patch("interface.product_interface._get_input", side_effect = ['    q', '       quit', '       Quit', '      QUIT'])
    def test_answer_leading_whitespace_quit(self, input):
        self.assertFalse(interface.product_interface._product_menu() == 'q' and
                        interface.product_interface._product_menu() == 'quit' and
                        interface.product_interface._product_menu() == 'Quit' and
                        interface.product_interface._product_menu() == 'QUIT')


if __name__ == "__main__":
    unittest.main()
