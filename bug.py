def function_with_uncommon_error(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None  # Or raise a custom exception
    except TypeError:
        print("Error: Unsupported operand type(s) for /: 'int' and 'str'")
        return None
    return result

# Example usage demonstrating both exceptions
print(function_with_uncommon_error(10, 0))  # ZeroDivisionError
print(function_with_uncommon_error(10, 'hello')) # TypeError
print(function_with_uncommon_error(10, 2))