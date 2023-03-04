import unittest
from fliniowa import fliniowa


class FliniowaTestCase(unittest.TestCase):
    def test_fl_1_6(self):
        value = 1
        expected = 6
        result = fliniowa(value)
        self.assertEqual(result, expected)

class FliniowaTestCase(unittest.TestCase):
    def test_fl_5_10(self):
        value = 5
        expected = 10
        result = fliniowa(value)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
