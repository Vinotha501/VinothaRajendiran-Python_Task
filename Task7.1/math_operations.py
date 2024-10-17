# math_operations

def add(a, b):
    result = a + b
    print(f"Adding {a} and {b} returns {result}")
    return result

def subtract(a, b):
    result = a - b
    print(f"Subtracting {a} and {b} returns {result}")
    return result

def multiply(a, b):
    result = a * b
    print(f"Multipling {a} and {b} returns {result}")
    return result

def divide(a, b):
    if b == 0:
        raise ValueError("Divivsion by zero is not defined.")
    result = a / b
    print(f"Dividing {a} and {b} returns{result}")
    return result
