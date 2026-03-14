# numbers.py - Version 3 (with bug)
# Reviewed by team: Fixed division bug
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b  # This will crash if b = 0!

print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))
print("Multiplication:", multiply(5, 3))
print("Division:", divide(5, 0))  # BUG: Division by zero!

import math

def square_root(a):
    if a < 0:
        return "Error: Cannot square root negative"
    return math.sqrt(a)

print("Square root of 25:", square_root(25))
