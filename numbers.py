# numbers.py - Version 3 (with bug)
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