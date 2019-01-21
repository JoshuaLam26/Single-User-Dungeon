from unittest import TestCase
import comp_1510_a1
from unittest.mock import patch
import json


class TestReload_game(TestCase):

    @patch('comp_1510_a1.get_user_name', return_value='reload_test_dont_modify')
    def test_reload_game(self, mock_get_user_name):

        # Create a new game
        original_game = comp_1510_a1.start_game()

        # Modify that game manually
        original_game["hp"] = 7
        original_game["row_loc"] = 2
        original_game["col_loc"] = 1
        original_game["sud_map"][0][0]['appearance'] = "[ ]"
        original_game["sud_map"][2][1]['appearance'] = "[X]"

        # Save game over the game we just created
        comp_1510_a1.save(original_game)

        # Check if the json values changed
        with open('reload_test_dont_modify.json') as file_object:
            content = json.load(file_object)
            self.assertEqual(7, content["hp"])
            self.assertEqual(2, content['row_loc'])
            self.assertEqual(1, content['col_loc'])
            self.assertEqual('[X]', content['sud_map'][2][1]['appearance'])

        # Reload the game
        comp_1510_a1.reload_game(original_game)

        # Check if the json values are back to default
        with open('reload_test_dont_modify.json') as file_object:
            content = json.load(file_object)
            self.assertEqual(10, content["hp"])
            self.assertEqual(0, content['row_loc'])
            self.assertEqual(0, content['col_loc'])
            self.assertEqual('[ ]', content['sud_map'][2][1]['appearance'])
            self.assertEqual('[X]', content['sud_map'][0][0]['appearance'])