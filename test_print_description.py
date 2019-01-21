from unittest import TestCase
import comp_1510_a1

class TestPrint_description(TestCase):

    def test_print_description_0_0(self):
        saved_game = {"username": 'Josh',
                      "hp": 10,
                      "row_loc": 0,
                      "col_loc": 0,
                      "sud_map": [[{"appearance": "[X]", "description": "00"},
                                   {"appearance": "[ ]", "description": "01"},
                                   {"appearance": "[ ]", "description": "02"},
                                   {"appearance": "[ ]", "description": "03"}],
                                  [{"appearance": "[ ]", "description": "10"},
                                   {"appearance": "[ ]", "description": "11"},
                                   {"appearance": "[ ]", "description": "12"},
                                   {"appearance": "[ ]", "description": "13"}],
                                  [{"appearance": "[ ]", "description": "20"},
                                   {"appearance": "[ ]", "description": "21"},
                                   {"appearance": "[ ]", "description": "22"},
                                   {"appearance": "[ ]", "description": "23"}],
                                  [{"appearance": "[ ]", "description": "30"},
                                   {"appearance": "[ ]", "description": "31"},
                                   {"appearance": "[ ]", "description": "32"},
                                   {"appearance": "[ ]", "description": "33"}]]
                      }
        self.assertEqual("   00", comp_1510_a1.print_description(saved_game))

    def test_print_description_3_3(self):
        saved_game = {"username": 'Josh',
                      "hp": 10,
                      "row_loc": 3,
                      "col_loc": 3,
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
                                   {"appearance": "[ ]", "description": "22"},
                                   {"appearance": "[ ]", "description": "23"}],
                                  [{"appearance": "[ ]", "description": "30"},
                                   {"appearance": "[ ]", "description": "31"},
                                   {"appearance": "[ ]", "description": "32"},
                                   {"appearance": "[X]", "description": "33"}]]
                      }
        self.assertEqual("   33", comp_1510_a1.print_description(saved_game))

    def test_print_description_2_1(self):
        saved_game = {"username": 'Josh',
                      "hp": 10,
                      "row_loc": 2,
                      "col_loc": 1,
                      "sud_map": [[{"appearance": "[X]", "description": "00"},
                                   {"appearance": "[ ]", "description": "01"},
                                   {"appearance": "[ ]", "description": "02"},
                                   {"appearance": "[ ]", "description": "03"}],
                                  [{"appearance": "[ ]", "description": "10"},
                                   {"appearance": "[ ]", "description": "11"},
                                   {"appearance": "[ ]", "description": "12"},
                                   {"appearance": "[ ]", "description": "13"}],
                                  [{"appearance": "[ ]", "description": "20"},
                                   {"appearance": "[ ]", "description": "21"},
                                   {"appearance": "[ ]", "description": "22"},
                                   {"appearance": "[ ]", "description": "23"}],
                                  [{"appearance": "[ ]", "description": "30"},
                                   {"appearance": "[ ]", "description": "31"},
                                   {"appearance": "[ ]", "description": "32"},
                                   {"appearance": "[ ]", "description": "33"}]]
                      }
        self.assertEqual("   21", comp_1510_a1.print_description(saved_game))
