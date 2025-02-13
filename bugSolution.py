def improved_function(a, b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise TypeError("Inputs must be numbers.")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

# Example usage
try:
    print(improved_function(10, 0))
except ZeroDivisionError as e:
    print(f"Error: {e}")
try:
    print(improved_function(10, "hello"))
except TypeError as e:
    print(f"Error: {e}")
try:
    print(improved_function(10, 2))
except Exception as e:
    print(f"An unexpected error occurred: {e}")
