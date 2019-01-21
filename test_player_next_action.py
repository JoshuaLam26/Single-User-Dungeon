from unittest import TestCase
import comp_1510_a1
from unittest.mock import patch

class TestPlayer_next_action(TestCase):

    saved_game = {"username": 'Josh',
                  "hp": 10,
                  "row_loc": 2,
                  "col_loc": 2,
                  "sud_map": [[{"appearance": "[ ]", "description": "00"},
                               {"appearance": "[ ]", "description": "01"},
                               {"appearance": "[ ]", "description": "02"},
                               {"appearance": "[ ]", "description": "03"}],
                              [{"appearance": "[ ]", "description": "10"},
                               {"appearance": "[ ]", "description": "11"},
                               {"appearance": "[ ]", "description": "12"},
                               {"appearance": "[ ]", "description": "13"}],
                              [{"appearance": "[ ]", "description": "20"},
                               {"appearance": "[ ]", "description": "21"},
                               {"appearance": "[X]", "description": "22"},
                               {"appearance": "[ ]", "description": "23"}],
                              [{"appearance": "[ ]", "description": "30"},
                               {"appearance": "[ ]", "description": "31"},
                               {"appearance": "[ ]", "description": "32"},
                               {"appearance": "[ ]", "description": "33"}]]
                  }

    @patch('builtins.input', return_value='q')
    def test_player_next_action_q(self, mock_input):
        self.assertEqual('q', comp_1510_a1.player_next_action(self.saved_game))

    @patch('builtins.input', return_value='n')
    @patch('comp_1510_a1.move_character', return_value=False)
    def test_player_next_action_n(self, mock_input, mock_move_character):
        self.assertEqual('n', comp_1510_a1.player_next_action(self.saved_game))

    @patch('builtins.input', return_value='e')
    @patch('comp_1510_a1.move_character', return_value=False)
    def test_player_next_action_e(self, mock_input, mock_move_character):
        self.assertEqual('e', comp_1510_a1.player_next_action(self.saved_game))

    @patch('builtins.input', return_value='s')
    @patch('comp_1510_a1.move_character', return_value=False)
    def test_player_next_action_s(self, mock_input, mock_move_character):
        self.assertEqual('s', comp_1510_a1.player_next_action(self.saved_game))

    @patch('builtins.input', return_value='w')
    @patch('comp_1510_a1.move_character', return_value=False)
    def test_player_next_action_w(self, mock_input, mock_move_character):
        self.assertEqual('w', comp_1510_a1.player_next_action(self.saved_game))

    @patch('builtins.input', side_effect=['d', ';', 'n'])
    @patch('comp_1510_a1.move_character', return_value=False)
    def test_player_next_action_miss_input(self, mock_input, mock_move_character):
        self.assertEqual('n', comp_1510_a1.player_next_action(self.saved_game))

