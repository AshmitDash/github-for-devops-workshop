"""
This module takes two numbers from the user and prints their sum.
"""

print("Hello world")

a = input("First Number: ")
b = input("\nSecond Number:")

c = float(a) + float(b)

# Replaced .format() with f-string for cleaner code
print(f"the sum of {a} and {b} is {c}")
