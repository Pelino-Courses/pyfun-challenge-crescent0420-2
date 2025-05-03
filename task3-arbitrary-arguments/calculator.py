"""
Performs basic arithmetic operations (add, subtract, multiply, divide) with optional rounding.

Parameters:
- operation (str): 'add', 'subtract', 'multiply', 'divide'.
- *args (float): Numbers for the operation.
- **kwargs:
  - round_result (bool): Whether to round the result (default: False).
  - precision (int): Decimal precision for rounding (default: 2).

Returns:
- float or int: The result of the operation.

Raises:
- ValueError: Invalid operation or missing arguments.
- TypeError: Non-numeric arguments.
"""

def add(*args):
    """Returns the sum of all arguments."""
    return sum(args)

def subtract(*args):
    """Subtracts all following arguments from the first."""
    if not args:
        raise ValueError("At least one number is required for subtraction.")
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    """Multiplies all arguments together."""
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    """Divides the first number by all subsequent numbers in order."""
    if not args:
        raise ValueError("At least one number is required for division.")
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result /= num
    return result

def calculate(operation, *args, **kwargs):
    """
    Performs a calculation based on the operation and numbers provided.

    Parameters:
        operation (str): One of 'add', 'subtract', 'multiply', or 'divide'.
        *args (float): Numbers to process.
        **kwargs:
            round_result (bool): Whether to round the result (default: False).
            precision (int): Number of decimal places to round to (default: 2).

    Returns:
        float or int: The result of the calculation.

    Raises:
        ValueError: If an invalid operation is specified or inputs are missing.
        TypeError: If non-numeric arguments are passed.
    """
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    if operation not in operations:
        raise ValueError(f"Unsupported operation '{operation}'. Choose from {list(operations.keys())}.")

    if not args:
        raise ValueError("At least one numeric argument is required.")

    # Ensure all arguments are numeric
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("All positional arguments must be numbers.")

    result = operations[operation](*args)

    # Handle keyword arguments
    if kwargs.get('round_result', False):
        precision = kwargs.get('precision', 2)
        if not isinstance(precision, int) or precision < 0:
            raise ValueError("Precision must be a non-negative integer.")
        result = round(result, precision)

    return result


# Example usage
if __name__ == "__main__":
    try:
        print("Addition:", calculate('add', 5, 1, 11))
        print("Subtraction:", calculate('subtract', 0, 5, 5))
        print("Multiplication:", calculate('multiply', 1, 3, 5))
        print("Division:", calculate('divide', 100, 5, round_result=True, precision=1))
    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f"Calculation error: {e}")
