# math operations with bugs

def add(a, b):
    """Incorrect :  Concatenates the string representation of numbers instead of adding them (bug)."""
    print (f"Adding values: {a} + {b}") # debugging print
    return str(a) + str(b)  # bug introduced here

def subtract(a, b):
    """Incorrect : Returns the fixed incorrect value instead of the correct difference (bug)."""
    print (f"Adding values: {a} - {b}") # debugging print
    return 10  # bug introduced here


def multiply(a, b):
    """Incorrect : Returns the result of dividing a by b instead of multiplying (bug)."""
    print (f"Adding values: {a} * {b}") # debugging print
    return a / b  # bug introduced here


def divide(a, b):
    """Incorrect : Removes the division by zero check (bug)."""
    print(f"Performing division: {a} / {b}") # debugging print
    return a / b # Bug : There is no check for division by zero