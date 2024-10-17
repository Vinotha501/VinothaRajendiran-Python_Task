# Decorators and Meta-programming
import time
from functools import wraps

# logging decorator
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        if result is not None:
           print(f"Function '{func.__name__}' returned: {result}")
        print()
        return result
    return wrapper

# Timing decorator
def time_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        if result is not None:
           print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute.")
        return result
    return wrapper

# Access control decorator
def access_control_decorator(allowed_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = kwargs.get("role", "guest")
            if user_role != allowed_role:
                print(f"Access denied for role: {user_role}")
                print()
                return None
            print(f"Access granted for role: {user_role}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Call count decorator
def count_calls_decorator(func):
    @wraps(func)
    def wrapper (*args, **kwargs):
        wrapper.call_count += 1
        print(f"Function '{func.__name__}' has been called {wrapper.call_count} times.")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@log_function_call
@time_function
@access_control_decorator("admin")
@count_calls_decorator
def example_function(x, y, role="guest"):
    return x + y

# Test function calls
print("Testing example functions:")
example_function(3, 5, role="admin")
example_function(2, 4, role="admin")
example_function(5, 2, role="user")

# Metaclass enforcing constraints
class RequiredMeta(type):
    def __new__(cls, name, bases, dct):
        if name != "Animal" and "speak" not in dct:
            raise TypeError(f"Class {name} must implement a 'speak' method.")
        return super().__new__(cls, name, bases, dct)

# Base class using metaclass
class Animal(metaclass=RequiredMeta):
    pass

# Correct usage
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Incorrect usage
try:
    class Dog(Animal):
        pass
except TypeError as e:
    print("Enforcing Method Constraints:")
    print(f"Error: {e}")

# metaclass with class registered
class RegisteredMeta(type):
    registry = {}

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        cls.registry[name] = new_class
        return new_class

    @classmethod
    def get_class(cls, name):
        return cls.registry.get(name)
    
class Baseclass(metaclass = RegisteredMeta):
    pass

class MyClass1(Baseclass):
    pass

class MyClass2(Baseclass):
    pass

print ("\nRegistered Classes:")
for name, cls in RegisteredMeta.registry.items():
     if name != "Baseclass":
        print (f"{name}: {cls}")

print("\nLookup by name:")
lookup_cls = RegisteredMeta.get_class("MyClass1")
print(f"Found Class: {lookup_cls}")