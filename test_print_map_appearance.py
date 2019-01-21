from unittest import TestCase
import comp_1510_a1


class TestPrint_map_appearance(TestCase):

    def test_print_map_appearance(self):
        saved_game = {"username": 'Josh',
                      "hp": 10,
                      "row_loc": 0,
                      "col_loc": 0,
                      "sud_map": [[{"appearance": "[X]", "description": ""}, {"appearance": "[ ]", "description": ""},
                                   {"appearance": "[ ]", "description": ""}, {"appearance": "[ ]", "description": ""}],
                                  [{"appearance": "[ ]", "description": ""}, {"appearance": "[ ]", "description": ""},
                                   {"appearance": "[ ]", "description": ""}, {"appearance": "[ ]", "description": ""}],
                                  [{"appearance": "[ ]", "description": ""}, {"appearance": "[ ]", "description": ""},
                                   {"appearance": "[ ]", "description": ""}, {"appearance": "[ ]", "description": ""}],
                                  [{"appearance": "[ ]", "description": ""}, {"appearance": "[ ]", "description": ""},
                                   {"appearance": "[ ]", "description": ""}, {"appearance": "[ ]", "description": ""}]]
                      }
        self.assertEqual("[X][ ][ ][ ]\n[ ][ ][ ][ ]\n[ ][ ][ ][ ]\n[ ][ ][ ][ ]\n",
                         comp_1510_a1.print_map_appearance(saved_game))
