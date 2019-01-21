from unittest import TestCase
import comp_1510_a1
from unittest.mock import patch


class TestFight(TestCase):

    @patch('random.randint', return_value=6)
    def test_fight_dino_die(self, mock_randint):
        game = {"username": 'Josh',
                "hp": 7,
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
        self.assertEqual(True, comp_1510_a1.fight(game))

    @patch('random.randint', return_value=2)
    def test_fight_character_die(self, mock_randint):
        game = {"username": 'Josh',
                "hp": 4,
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
        self.assertEqual(False, comp_1510_a1.fight(game))
