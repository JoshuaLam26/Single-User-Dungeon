from unittest import TestCase
import comp_1510_a1


class TestLoad_descriptions(TestCase):

    def test_load_descriptions(self):
        sud_map = [[{"appearance": "", "description": ""}, {"appearance": "", "description": ""},
                    {"appearance": "", "description": ""}, {"appearance": "", "description": ""}],
                   [{"appearance": "", "description": ""}, {"appearance": "", "description": ""},
                    {"appearance": "", "description": ""}, {"appearance": "", "description": ""}],
                   [{"appearance": "", "description": ""}, {"appearance": "", "description": ""},
                    {"appearance": "", "description": ""}, {"appearance": "", "description": ""}],
                   [{"appearance": "", "description": ""}, {"appearance": "", "description": ""},
                    {"appearance": "", "description": ""}, {"appearance": "", "description": ""}]]
        comp_1510_a1.load_descriptions(sud_map)
        # testing each cell to see if their description has changed
        self.assertEqual("You are in the park entrance and hear loud stomps getting closer. You better get moving!",
                         sud_map[0][0]["description"])
        self.assertEqual("You walked into the main observatory. There is debris all over the place. Watch your step.",
                         sud_map[0][1]["description"])
        self.assertEqual("You enter the kitchen and see a dinosaur's shadows on the wall. "
                         "Quick try and hide in the cupboard.",
                         sud_map[0][2]["description"])
        self.assertEqual("Look the rescue helicopter is over there, but it cant find a safe spot to land. "
                         "You better keep moving.",
                         sud_map[0][3]["description"])
        self.assertEqual("Ewww what is that smell? You look around and find a pile of half eaten human bodies.",
                         sud_map[1][0]["description"])
        self.assertEqual("*RAWR* That must be a T-Rex! Get out of here!",
                         sud_map[1][1]["description"])
        self.assertEqual("You hide in a porta potty. It stinks, but it beats getting eaten.",
                         sud_map[1][2]["description"])
        self.assertEqual("Look some hunting rifles. It wouldn't be a bad idea to take these.",
                         sud_map[1][3]["description"])
        self.assertEqual("'Hey man, can you help us?' You run into some other survivors.",
                         sud_map[2][0]["description"])
        self.assertEqual("You see a car and start its engine. The engine is loud... "
                         "maybe that wasn't such a good idea.",
                         sud_map[2][1]["description"])
        self.assertEqual("You made it to the rendezvous point. Hopefully the helicopter gets here soon!",
                         sud_map[2][2]["description"])
        self.assertEqual("There's a pack of velociraptors up ahead. Quick hide behind some trees.",
                         sud_map[2][3]["description"])
        self.assertEqual("You're under a car hiding from a T-Rex, cover yourself in oil so he can't smell you.",
                         sud_map[3][0]["description"])
        self.assertEqual("You try using your phone to call for help, but you can't get any reception.",
                         sud_map[3][1]["description"])
        self.assertEqual("*ouch* You roll your ankle in a pot hole.",
                         sud_map[3][2]["description"])
        self.assertEqual("You feel like this is hopeless and roll up into a ball crying.",
                         sud_map[3][3]["description"])

