from unittest import TestCase
import comp_1510_a1

class TestMove_character(TestCase):

    def test_move_character_n(self):
        game = {"username": 'Josh',
                "hp": 10,
                "row_loc": 1,
                "col_loc": 0,
                "sud_map": [[{"appearance": "[ ]", "description": "00"}, {"appearance": "[ ]", "description": "01"},
                             {"appearance": "[ ]", "description": "02"}, {"appearance": "[ ]", "description": "03"}],
                            [{"appearance": "[X]", "description": "10"}, {"appearance": "[ ]", "description": "11"},
                             {"appearance": "[ ]", "description": "12"}, {"appearance": "[ ]", "description": "13"}],
                            [{"appearance": "[ ]", "description": "20"}, {"appearance": "[ ]", "description": "21"},
                             {"appearance": "[ ]", "description": "22"}, {"appearance": "[ ]", "description": "23"}],
                            [{"appearance": "[ ]", "description": "30"}, {"appearance": "[ ]", "description": "31"},
                             {"appearance": "[ ]", "description": "32"}, {"appearance": "[ ]", "description": "33"}]]
                }
        # Character will move north from [1,0] to [0,0], move_character will turn True
        self.assertEqual(True, comp_1510_a1.move_character('n', game))
        # Character cant move farther north than [0,0], move_character will turn False
        self.assertEqual(False, comp_1510_a1.move_character('n', game))

    def test_move_character_e(self):
        game = {"username": 'Josh',
                "hp": 10,
                "row_loc": 0,
                "col_loc": 2,
                "sud_map": [[{"appearance": "[ ]", "description": "00"}, {"appearance": "[ ]", "description": "01"},
                             {"appearance": "[X]", "description": "02"}, {"appearance": "[ ]", "description": "03"}],
                            [{"appearance": "[ ]", "description": "10"}, {"appearance": "[ ]", "description": "11"},
                             {"appearance": "[ ]", "description": "12"}, {"appearance": "[ ]", "description": "13"}],
                            [{"appearance": "[ ]", "description": "20"}, {"appearance": "[ ]", "description": "21"},
                             {"appearance": "[ ]", "description": "22"}, {"appearance": "[ ]", "description": "23"}],
                            [{"appearance": "[ ]", "description": "30"}, {"appearance": "[ ]", "description": "31"},
                             {"appearance": "[ ]", "description": "32"}, {"appearance": "[ ]", "description": "33"}]]
                }
        # Character will move east from [0,2] to [0,3], move_character will turn True
        self.assertEqual(True, comp_1510_a1.move_character('e', game))
        # Character cant move farther east than [0,3], move_character will turn False
        self.assertEqual(False, comp_1510_a1.move_character('e', game))

    def test_move_character_s(self):
        game = {"username": 'Josh',
                "hp": 10,
                "row_loc": 2,
                "col_loc": 0,
                "sud_map": [[{"appearance": "[ ]", "description": "00"}, {"appearance": "[ ]", "description": "01"},
                             {"appearance": "[ ]", "description": "02"}, {"appearance": "[ ]", "description": "03"}],
                            [{"appearance": "[ ]", "description": "10"}, {"appearance": "[ ]", "description": "11"},
                             {"appearance": "[ ]", "description": "12"}, {"appearance": "[ ]", "description": "13"}],
                            [{"appearance": "[X]", "description": "20"}, {"appearance": "[ ]", "description": "21"},
                             {"appearance": "[ ]", "description": "22"}, {"appearance": "[ ]", "description": "23"}],
                            [{"appearance": "[ ]", "description": "30"}, {"appearance": "[ ]", "description": "31"},
                             {"appearance": "[ ]", "description": "32"}, {"appearance": "[ ]", "description": "33"}]]
                }
        # Character will move south from [2,0] to [3,0], move_character will turn True
        self.assertEqual(True, comp_1510_a1.move_character('s', game))
        # Character cant move farther south than [3,0], move_character will turn False
        self.assertEqual(False, comp_1510_a1.move_character('s', game))

    def test_move_character_w(self):
        game = {"username": 'Josh',
                "hp": 10,
                "row_loc": 0,
                "col_loc": 1,
                "sud_map": [[{"appearance": "[ ]", "description": "00"}, {"appearance": "[X]", "description": "01"},
                             {"appearance": "[ ]", "description": "02"}, {"appearance": "[ ]", "description": "03"}],
                            [{"appearance": "[ ]", "description": "10"}, {"appearance": "[ ]", "description": "11"},
                             {"appearance": "[ ]", "description": "12"}, {"appearance": "[ ]", "description": "13"}],
                            [{"appearance": "[ ]", "description": "20"}, {"appearance": "[ ]", "description": "21"},
                             {"appearance": "[ ]", "description": "22"}, {"appearance": "[ ]", "description": "23"}],
                            [{"appearance": "[ ]", "description": "30"}, {"appearance": "[ ]", "description": "31"},
                             {"appearance": "[ ]", "description": "32"}, {"appearance": "[ ]", "description": "33"}]]
                }
        # Character will move west from 01 to 00, move_character will turn true
        self.assertEqual(True, comp_1510_a1.move_character('w', game))
        # Character cant move farther west than 00, move_character will turn False
        self.assertEqual(False, comp_1510_a1.move_character('w', game))
