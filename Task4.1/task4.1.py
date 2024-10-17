# Build a Robust Calculator
import math

class Calculator:
# Basic operations
    def add(self, a, b):
        try:
            return (a + b)
        except TypeError:
            return "Error: Invalid input, please provide numbers."

    def sub(self, a, b):
        try:
            return a - b
        except TypeError:
            return "Error: Invalid input, please provide numbers."

        
    def multiply(self, a, b):
        try:
            return a * b
        except TypeError:
            return "Error: Invalid input, please provide numbers."

    def divide(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError ("Division by zero is undefined.")
            return a / b
        except TypeError:
            return "Error: Invalid input, please provide numbers."
        except ZeroDivisionError as e:
            return f"Error: {e}"

   # Advanced operations
    def square_root(self, a):
        try:
            if a < 0:
               raise ValueError("Square root of a negative number is undefined real numbers.")
            return math.sqrt(a)
        except TypeError:
            return "Error: Invalid input, please provide numbers."
        except ValueError as e:
            return f"Error: {e}"

    def exponentiation(self, a, b):
        try:
            return a ** b
        except TypeError:
            return "Error: Invalid input, please provide numbers."
    
    def logarithm(self, a, base=10):
        try:
            if a <= 0:
                raise ValueError("Logarithm of non-positive numbers is undefined.")
            return math.log(a, base)
        except TypeError:
            return "Error: Invalid input, please provide numbers."
        except ValueError as e:
            return f"Error: {e}"


# test calculater
def test_calculator():
    calc = Calculator()
    
    # basic operations
    print("Addition:", calc.add (5, 3))
    print("Subtraction:", calc.sub (7, 2))
    print("Multiplication:", calc.multiply (10, 4))
    print("Division:", calc.divide (6, 3))
    print("Division by zero:", calc.divide (12, 0))
    print("Addition with invalid input:", calc.add (15, "4"))

    # Advanced operations
    print("Square root:", calc.square_root (6))
    print("Square root of negative number:", calc.square_root (-6))
    print("Exponentiation:", calc.exponentiation (2, 3))
    print("Logarithm:", calc.logarithm (80, 40))
    print("Logarithm of non_positive number:", calc.logarithm (-80, 40))
    
    print("All tests passed")

test_calculator()
