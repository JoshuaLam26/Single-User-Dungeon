from unittest import TestCase
import comp_1510_a1


class TestPrint_scenario(TestCase):

    def test_print_scenario(self):
        self.assertEqual("Idea Credit: Jurassic Park by Steven Spielberg"
                         "\n          You are one of the lucky few who had the opportunity "
                         "to visit the dinosaur island theme park, Jurassic Park!"
                         "\n          During your visit the park's power went down and some of the dinosaurs escaped."
                         "\n          Run around the park until the rescue helicopter can pick you up."
                         "\n          Survive using any means possible. Good Luck!", comp_1510_a1.print_scenario())
