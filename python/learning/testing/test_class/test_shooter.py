# setUp() - runs before each method
# tearDown() - runs after each method
import unittest
from shooter import Shooter


class ShooterTest(unittest.TestCase):
    """
    Test class Shooter from shooter.py
    """

    mock_data = []

    def setUp(self):
        self.jake = Shooter('Jack')
        print(self.mock_data)
        self.mock_data = [1, 2, 3, 4, 5]

    def tearDown(self):
        print(self.mock_data)
        self.mock_data = []

    def test_get_cash(self):
        # jake = Shooter('Jack')  # setUp
        self.jake.get_cash(500)
        self.assertEqual(self.jake.money, 1500)
        print(self.mock_data)

    def test_greet(self):
        # jake = Shooter('Jack')  # setUp
        self.assertEqual(self.jake.greet(), 'Hello! How are you?')
        self.jake.money = 50
        self.assertEqual(self.jake.greet(), 'Hello! I need cash')


if __name__ == '__main__':
    unittest.main()
