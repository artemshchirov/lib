# TDD - Test Drive Development
import unittest
import cool_game


class CoolGameFunctionsTest(unittest.TestCase):
    def test_greet(self):
        """
        greet() have to return 'How are you?' if isEnemy == False
        """
        self.assertEqual(cool_game.greet('Jack', False), 'Hello Jack! How are you?')

    def test_greet_enemy(self):
        """
        greet() have to return 'I will kill you!' if isEnemy == True
        """
        self.assertEqual(cool_game.greet('Ivan', True), 'Hello Ivan! I will kill you!')

    def test_greet_enemy_boolean(self):
        """
        assertRaises
        """
        with self.assertRaises(ValueError):
            cool_game.greet('Ivan', 'Bla-Bla')

    def test_eat_burgers(self):
        """
        eat_burgers() have to return 'Mmm! That was excellent!' if number <= 3
        """
        self.assertEqual(cool_game.eat_burgers(3), 'Mmm! That was excellent!')

    def test_overeat_burgers(self):
        """
        eat_burgers() have to return 'Ohh! I overate!' if number > 3
        """
        self.assertEqual(cool_game.eat_burgers(4), 'Ohh! I overate!')

    def test_can_fly_batman(self):
        """
        can_fly() have to return True if name == 'Batman'
        """
        self.assertTrue(cool_game.can_fly('Batman'), 'Batman have be able to fly')

    def test_can_fly_anyone_else(self):
        """
        can_fly() have to return True if name != 'Batman'
        """
        self.assertEqual(cool_game.can_fly('Bob'), False)
        self.assertEqual(cool_game.can_fly('Jim'), False)
        self.assertEqual(cool_game.can_fly('Kevin'), False)

    def test_get_arsenal(self):
        """
        get_arsenal() have to return something one from ('knife', 'handgun', 'machine gun')
        """
        self.assertIn(cool_game.get_arsenal(), ('knife', 'handgun', 'machine gun'))


if __name__ == '__main__':
    unittest.main()
