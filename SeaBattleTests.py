from SeaBattle import FieldPart, Color, Game
import unittest


class SeaBattleTest(unittest.TestCase):
    def test_FieldPart(self):
        self.assertEqual(FieldPart.main, 'map')
        self.assertEqual(FieldPart.radar, 'radar')
        self.assertEqual(FieldPart.weight, 'weight')

    def test_Color(self):
        self.assertEqual(Color.yellow2, '\033[1;35m')
        self.assertEqual(Color.reset, '\033[0m')
        self.assertEqual(Color.blue, '\033[0;34m')
        self.assertEqual(Color.yellow, '\033[1;93m')
        self.assertEqual(Color.red, '\033[1;93m')
        self.assertEqual(Color.miss, '\033[0;37m')

    def test_Game(self):
        self.assertEqual(Game.letters, ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J"))
        self.assertEqual(Game.ships_rules, [1, 1, 1, 1, 2, 2, 2, 3, 3, 4])

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
