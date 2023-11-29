import unittest
from src.add import Addition
from src.sub import Subtraction

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        addition = Addition()
        result = addition.perform(5, 3)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        subtraction = Subtraction()
        result = subtraction.perform(5, 3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
