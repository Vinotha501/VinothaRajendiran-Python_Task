from my_package123.file_utils import read_file, write_file, append_file
from my_package123.math_utils import add, subtract, multiply, divide
from my_package123.string_utils import uppercase, reverse_string, count_vowels

# File operations
print("File Operations:")
write_file('somefile.txt', 'Hello!')
append_file('somefile.txt', ' Appended Text')
content = read_file('somefile.txt')
print(f"File content: {content}")

# Math operations
print("\nMath Operations:")
print(f"Add: {add(1, 2)}")
print(f"Subtract: {subtract(5, 3)}")
print(f"Multiply: {multiply(4, 2)}")
print(f"Divide: {divide(6, 3)}")

# String operations
print("\nString Operations:")
print(f"Uppercase: {uppercase('hello')}")
print(f"Reversed: {reverse_string('hello')}")
print(f"Vowel count: {count_vowels('hello')}")

