# This script demonstrates a simple division operation with proper error handling.

from typing import Optional


def divide(a: int, b: int) -> Optional[float]:
    """
    Divide two numbers represented as integers and handle errors gracefully.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        Optional[float]: The result of the division if successful, None otherwise.
    """

    try:
        # Perform division
        return a / b
    except ValueError:
        print(f'Invalid input: {a} or {b} is not an integer.')
        return None
    except ZeroDivisionError:
        print('Error: Division by zero is not allowed.')
        return None


if __name__ == '__main__':
    result = divide(22, 0)
    if result is not None:
        print(result)
    else:
        print('Division could not be performed.')