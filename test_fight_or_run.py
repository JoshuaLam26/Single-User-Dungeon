from unittest import TestCase
import comp_1510_a1
from unittest.mock import patch


class TestFight_or_run(TestCase):

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

    @patch('builtins.input', return_value="r")
    def test_fight_or_run_r_lower(self, mock_input):
        self.assertEqual(True, comp_1510_a1.fight_or_run(self.game))

    @patch('builtins.input', return_value="R")
    def test_fight_or_run_r_upper(self, mock_input):
        self.assertEqual(True, comp_1510_a1.fight_or_run(self.game))

    @patch('builtins.input', return_value="   R   ")
    def test_fight_or_run_whitespace(self, mock_input):
        self.assertEqual(True, comp_1510_a1.fight_or_run(self.game))

    @patch('builtins.input', return_value="f")
    def test_fight_or_run_f_lower(self, mock_input):
        self.assertEqual(False, comp_1510_a1.fight_or_run(self.game))

    @patch('builtins.input', return_value="F")
    def test_fight_or_run_f_upper(self, mock_input):
        self.assertEqual(False, comp_1510_a1.fight_or_run(self.game))

    @patch('builtins.input', side_effect=['s', 'g', '1', "F"])
    def test_fight_or_run_miss_inputs(self, mock_input):
        self.assertEqual(False, comp_1510_a1.fight_or_run(self.game))


