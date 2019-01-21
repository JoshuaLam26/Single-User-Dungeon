from unittest import TestCase
import comp_1510_a1
from unittest.mock import patch


class TestStart_game(TestCase):

    @patch('comp_1510_a1.get_user_name', return_value='start_test_new_dont_modify')
    def test_start_game_create(self, mock_input):
        self.assertEqual({"username": "start_test_new_dont_modify", "hp": 10, "row_loc": 0, "col_loc": 0,
                          "sud_map": [[{"appearance": "[X]", "description": "You are in the park entrance and hear "
                                                                            "loud stomps getting closer. "
                                                                            "You better get moving!"},
                                       {"appearance": "[ ]", "description": "You walked into the main observatory. "
                                                                            "There is debris all over the place. "
                                                                            "Watch your step."},
                                       {"appearance": "[ ]", "description": "You enter the kitchen and see a "
                                                                            "dinosaur's shadows on the wall. "
                                                                            "Quick try and hide in the cupboard."},
                                       {"appearance": "[ ]", "description": "Look the rescue helicopter is over there, "
                                                                            "but it cant find a safe spot to land. "
                                                                            "You better keep moving."}],
                                      [{"appearance": "[ ]", "description": "Ewww what is that smell?"
                                                                            " You look around and find a pile "
                                                                            "of half eaten human bodies."},
                                       {"appearance": "[ ]", "description": "*RAWR* That must be a T-Rex! "
                                                                            "Get out of here!"},
                                       {"appearance": "[ ]", "description": "You hide in a porta potty. "
                                                                            "It stinks, but it beats getting eaten."},
                                       {"appearance": "[ ]", "description": "Look some hunting rifles. It wouldn't "
                                                                            "be a bad idea to take these."}],
                                      [{"appearance": "[ ]", "description": "'Hey man, can you help us?' "
                                                                            "You run into some other survivors."},
                                       {"appearance": "[ ]", "description": "You see a car and start its engine. "
                                                                            "The engine is loud... "
                                                                            "maybe that wasn't such a good idea."},
                                       {"appearance": "[ ]", "description": "You made it to the rendezvous point. "
                                                                            "Hopefully the helicopter gets here soon!"},
                                       {"appearance": "[ ]", "description": "There's a pack of velociraptors up ahead. "
                                                                            "Quick hide behind some trees."}],
                                      [{"appearance": "[ ]", "description": "You're under a car hiding from a T-Rex, "
                                                                            "cover yourself in oil "
                                                                            "so he can't smell you."},
                                       {"appearance": "[ ]", "description": "You try using your phone to call for "
                                                                            "help, but you can't get any reception."},
                                       {"appearance": "[ ]", "description": "*ouch* You roll your "
                                                                            "ankle in a pot hole."},
                                       {"appearance": "[ ]", "description": "You feel like this is hopeless "
                                                                            "and roll up into a ball crying."}]]}
                         , comp_1510_a1.start_game())

    @patch('comp_1510_a1.get_user_name', return_value='start_test_old_dont_modify')
    def test_start_game_open(self, mock_input):
        self.assertEqual({"username": "start_test_old_dont_modify", "hp": 10, "row_loc": 2, "col_loc": 2,
                          "sud_map": [[{"appearance": "[ ]", "description": "You are in the park entrance and hear "
                                                                            "loud stomps getting closer. "
                                                                            "You better get moving!"},
                                       {"appearance": "[ ]", "description": "You walked into the main observatory. "
                                                                            "There is debris all over the place. "
                                                                            "Watch your step."},
                                       {"appearance": "[ ]", "description": "You enter the kitchen and see a "
                                                                            "dinosaur's shadows on the wall. "
                                                                            "Quick try and hide in the cupboard."},
                                       {"appearance": "[ ]", "description": "Look the rescue helicopter is over there, "
                                                                            "but it cant find a safe spot to land. "
                                                                            "You better keep moving."}],
                                      [{"appearance": "[ ]", "description": "Ewww what is that smell?"
                                                                            " You look around and find a pile "
                                                                            "of half eaten human bodies."},
                                       {"appearance": "[ ]", "description": "*RAWR* That must be a T-Rex! "
                                                                            "Get out of here!"},
                                       {"appearance": "[ ]", "description": "You hide in a porta potty. "
                                                                            "It stinks, but it beats getting eaten."},
                                       {"appearance": "[ ]", "description": "Look some hunting rifles. It wouldn't "
                                                                            "be a bad idea to take these."}],
                                      [{"appearance": "[ ]", "description": "'Hey man, can you help us?' "
                                                                            "You run into some other survivors."},
                                       {"appearance": "[ ]", "description": "You see a car and start its engine. "
                                                                            "The engine is loud... "
                                                                            "maybe that wasn't such a good idea."},
                                       {"appearance": "[X]", "description": "You made it to the rendezvous point. "
                                                                            "Hopefully the helicopter gets here soon!"},
                                       {"appearance": "[ ]", "description": "There's a pack of velociraptors up ahead. "
                                                                            "Quick hide behind some trees."}],
                                      [{"appearance": "[ ]", "description": "You're under a car hiding from a T-Rex, "
                                                                            "cover yourself in oil "
                                                                            "so he can't smell you."},
                                       {"appearance": "[ ]", "description": "You try using your phone to call for "
                                                                            "help, but you can't get any reception."},
                                       {"appearance": "[ ]", "description": "*ouch* You roll your "
                                                                            "ankle in a pot hole."},
                                       {"appearance": "[ ]", "description": "You feel like this is hopeless "
                                                                            "and roll up into a ball crying."}]]}
                         , comp_1510_a1.start_game())
