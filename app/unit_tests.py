import unittest
from subModule.myModule import square


class TestStringMethods(unittest.TestCase):

    def test_squared(self):
        self.assertEqual(4, square(2))


if __name__ == '__main__':
    unittest.main()