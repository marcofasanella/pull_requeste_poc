# This script demonstrates a simple division operation with proper error handling.
from typing import Optional

def divide(a: str, b: str) -> Optional[float]:
    \"\"\
    Divide two numbers represented as strings and handle errors gracefully.

    Args:
        a (str): The numerator as a string.
        b (str): The denominator as a string.

    Returns:
        Optional[float]: The result of the division if successful, None otherwise.
    \"\"\
    try:
        # Convert input strings to integers
        num_a = int(a)
        num_b = int(b)

        # Perform division
        return num_a / num_b
    except ValueError:
        print(f'Invalid input: {a} or {b} is not a number.')
        return None
    except ZeroDivisionError:
        print('Error: Division by zero is not allowed.')
        return None


if __name__ == '__main__':
    result = divide('22', '0')
    if result is not None:
        print(result)
    else:
        print('Division could not be performed.')