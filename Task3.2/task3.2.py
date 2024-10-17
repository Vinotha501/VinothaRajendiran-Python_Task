# Create Custom Decorators

import time
from functools import wraps

# timing decorator
def timing_decorator(func):
    @wraps(func)
    def wrapper (*args, **kwargs):
        start_time = time.time()
        result = func (*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time
    return wrapper


# logger_decorator
def logger_decorator(func):
    @wraps(func)
    def wrapper (*args, **kwargs):

        # logging the function name and arguments
        print(f"Calling {func.__name__} with arguments: {args}, kwargs : {kwargs}")

        # calling the original function
        result, execution_time = func(*args, **kwargs)

        # logging the return value
        print (f"{func.__name__} returned : {result}")
        print(f"Iteration took {execution_time: 4f} seconds to execute.")
        print()
        return result, execution_time
    return wrapper

# parameterized decorator
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total_start_time = time.time()
            total_execution_time = 0

            for i in range(n):
               print (f"Iteration {i + 1} of {n}")
               result, iteration_execution_time = logger_decorator(timing_decorator(func))(*args, **kwargs)

            total_execution_time += iteration_execution_time

            total_end_time = time.time()
            total_execution_time = total_end_time - total_start_time
            print(f"Total execution time for {func.__name__}: {total_execution_time:4f} seconds")

            return result
        return wrapper
    return decorator


@repeat(3)
def multiple_numbers(x, y):
    time.sleep(2)
    return x + y

result = multiple_numbers(40, 20)
print ("Result :", result)


       