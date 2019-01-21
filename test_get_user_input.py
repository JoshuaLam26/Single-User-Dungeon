from unittest import TestCase
import comp_1510_a1
from unittest.mock import patch


class TestGet_user_input(TestCase):

    @patch('builtins.input', return_value="Josh")
    def test_get_user_input_normal(self, mock_input):
        self.assertEqual("Josh", comp_1510_a1.get_user_input())

    @patch('builtins.input', return_value="   Josh   ")
    def test_get_user_input_whitespace(self, mock_input):
        self.assertEqual("   Josh   ", comp_1510_a1.get_user_input())

    @patch('builtins.input', return_value="Josh lam")
    def test_get_user_input_multiple_words(self, mock_input):
        self.assertEqual("Josh lam", comp_1510_a1.get_user_input())

    @patch('builtins.input', side_effect=['><', '   ', 'josh lam'])
    def test_get_user_input_invalid_name(self, mock_input):
        self.assertEqual("josh lam", comp_1510_a1.get_user_input())
