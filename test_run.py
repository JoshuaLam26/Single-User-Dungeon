from unittest import TestCase
import comp_1510_a1
from unittest.mock import patch


class TestRun(TestCase):

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

    @patch('random.random', return_value=0.5)
    def test_run_escape_successfully(self, mock_random):
        # set hp to 7
        self.game["hp"] = 7
        # Assuring that the characters hp is 7
        self.assertEqual(7, self.game["hp"])
        # run() and get away without taking damage
        comp_1510_a1.run(self.game)
        # Assure that the characters hp is still 7 after running successfully
        self.assertEqual(7, self.game["hp"])

    @patch('random.random', return_value=0.01)
    @patch('random.randint', return_value=2)
    def test_run_caught(self, mock_rand, mock_randint):
        # Assuring that the characters hp is 7
        self.assertEqual(7, self.game["hp"])
        # run(), get caught, and take 2 damage
        comp_1510_a1.run(self.game)
        # Assure that the character is equal to 5 after taking 2 damage
        self.assertEqual(5, self.game["hp"])

