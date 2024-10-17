# test_math_operations

import unittest
from math_operations_debug import add, subtract, multiply, divide
#from math_operations_bugs import add, subtract, multiply, divide
#from math_operations import add, subtract, multiply, divide


class TestMathOperations(unittest.TestCase):

    def test_add(self):
        print("\nTesting addition...")
        self.assertEqual(add(4, 1), 5)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(-3, -4), -7)

    def test_subtract(self):
        print("\nTesting subtraction...")
        self.assertEqual(subtract(3, 1), 2)
        self.assertEqual(subtract(-3, 5), -8)
        self.assertEqual(subtract(5, -4), 9)

    def test_multiply(self):
        print("\nTesting multiplication...")
        self.assertEqual(multiply(4, 8), 32)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(-3, -4), 12)
        self.assertEqual(multiply(6, 0), 0)

    def test_divide(self):
        print("\nTesting division...")
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-10, 5), -2)
        self.assertEqual(divide(10, -5), -2)
        try:
            divide(10, 0)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    unittest.main()
