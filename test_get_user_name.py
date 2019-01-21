from unittest import TestCase
import comp_1510_a1
from unittest.mock import patch


class TestGet_user_name(TestCase):

    @patch('comp_1510_a1.get_user_input', return_value='Josh')
    def test_get_user_name_normal(self, mock_input):
        self.assertEqual('Josh', comp_1510_a1.get_user_name())

    @patch('comp_1510_a1.get_user_input', return_value='       Josh         ')
    def test_get_user_name_whitespace(self, mock_input):
        self.assertEqual('Josh', comp_1510_a1.get_user_name())

    @patch('comp_1510_a1.get_user_input', return_value='jOsh')
    def test_get_user_name_weird_caps(self, mock_input):
        self.assertEqual('Josh', comp_1510_a1.get_user_name())

    @patch('comp_1510_a1.get_user_input', return_value='josh lam')
    def test_get_user_name_two_names(self, mock_input):
        self.assertEqual('Josh Lam', comp_1510_a1.get_user_name())
