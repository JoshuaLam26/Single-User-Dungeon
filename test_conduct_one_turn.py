from unittest import TestCase
import comp_1510_a1
from unittest.mock import patch


class TestConduct_one_turn(TestCase):

    game = {"username": 'Josh',
            "hp": 10,
            "row_loc": 0,
            "col_loc": 0,
            "sud_map": [[{"appearance": "[X]", "description": "00"}, {"appearance": "[ ]", "description": "01"},
                         {"appearance": "[ ]", "description": "02"}, {"appearance": "[ ]", "description": "03"}],
                        [{"appearance": "[ ]", "description": "10"}, {"appearance": "[ ]", "description": "11"},
                         {"appearance": "[ ]", "description": "12"}, {"appearance": "[ ]", "description": "13"}],
                        [{"appearance": "[ ]", "description": "20"}, {"appearance": "[ ]", "description": "21"},
                         {"appearance": "[ ]", "description": "22"}, {"appearance": "[ ]", "description": "23"}],
                        [{"appearance": "[ ]", "description": "30"}, {"appearance": "[ ]", "description": "31"},
                         {"appearance": "[ ]", "description": "32"}, {"appearance": "[ ]", "description": "33"}]]
            }

    @patch('comp_1510_a1.player_next_action', return_value='n')
    def test_conduct_one_turn_character_moved_north(self, mock_player_next_action):
        self.assertEqual('n', comp_1510_a1.conduct_one_turn(self.game))

    @patch('comp_1510_a1.player_next_action', return_value='e')
    def test_conduct_one_turn_character_moved_east(self, mock_player_next_action):
        self.assertEqual('e', comp_1510_a1.conduct_one_turn(self.game))

    @patch('comp_1510_a1.player_next_action', return_value='s')
    def test_conduct_one_turn_character_moved_south(self, mock_player_next_action):
        self.assertEqual('s', comp_1510_a1.conduct_one_turn(self.game))

    @patch('comp_1510_a1.player_next_action', return_value='w')
    def test_conduct_one_turn_character_moved_west(self, mock_player_next_action):
        self.assertEqual('w', comp_1510_a1.conduct_one_turn(self.game))

    @patch('comp_1510_a1.player_next_action', return_value='q')
    def test_conduct_one_turn_quit(self, mock_player_next_action):
        self.assertEqual('q', comp_1510_a1.conduct_one_turn(self.game))
