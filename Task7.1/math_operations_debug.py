# math operations with debugging

def add(a, b):
    """Correctly returns the sum of a and b."""
    result = a + b
    print(f"[DEBUG - Add] Adding values: {a} + {b} = {result}") 
    return result 

def subtract(a, b):
    """Correctly returns the subtraction of a from b."""
    result = a - b
    print(f"[DEBUG - Subtract] Subtracting values: {a} - {b} = {result}")  
    return result

def multiply(a, b):
    """Correctly returns the product of a and b."""
    result = a * b
    print(f"[DEBUG - Multiply] Multiplying values: {a} * {b} = {result}")  
    return result

def divide(a, b):
    """Checks for division by zero and returns the division result."""
    if b == 0:
        raise ValueError("Division by zero is not defined.")
    result = a / b
    print(f"[DEBUG - Divide] Performing division: {a} / {b} = {result}")  
    return result 

