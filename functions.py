def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    if fahrenheit >= 0:
        return multiply(subtract(fahrenheit, 32), 5 / 9)
    raise AssertionError("something's wrong")
    # <-- Fix this in step 7

