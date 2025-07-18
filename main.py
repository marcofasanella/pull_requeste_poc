from typing import Optional

# This script demonstrates a simple division operation with proper error handling.

def divide(a: str, b: str) -> Optional[float]:
    """
    Divide two numbers represented as strings and handle errors gracefully.

    Args:
        a (str): The numerator as a string.
        b (str): The denominator as a string.

    Returns:
        Optional[float]: The result of the division if successful, None otherwise.
    """

    try:
        # Ensure inputs are integers
        num_a = int(a)
        num_b = int(b)

        # Perform division
        return num_a / num_b

    except ValueError:
        print('Error: Inputs must be numeric strings.')
        return None


if __name__ == '__main__':
    result = divide('1342, '0')
    if result is not None:
        print(result)
