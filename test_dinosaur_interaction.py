from unittest import TestCase
import comp_1510_a1
from unittest.mock import patch


class TestDinosaur_interaction(TestCase):

    @patch('random.random', return_value=0.5)
    def test_dinosaur_interaction_no_encounter_max_hp(self, mock_random):
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
        self.assertEqual(False, comp_1510_a1.dinosaur_interaction(game))
        self.assertEqual(10, game['hp'])

    @patch('random.random', return_value=0.5)
    def test_dinosaur_interaction_no_encounter_gain_one_hp(self, mock_random):
        game = {"username": 'Josh',
                "hp": 9,
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
        self.assertEqual(9, game['hp'])
        self.assertEqual(False, comp_1510_a1.dinosaur_interaction(game))
        self.assertEqual(10, game['hp'])

    @patch('random.random', return_value=0.01)
    @patch('comp_1510_a1.fight_or_run', return_value=True)
    def test_dinosaur_interaction_encounter(self, mock_random, mock_fight_or_run):
        game = {"username": 'Josh',
                "hp": 9,
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
        self.assertEqual(True, comp_1510_a1.dinosaur_interaction(game))
