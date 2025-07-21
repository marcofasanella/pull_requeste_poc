# This script demonstrates a simple division operation with proper error handling.

import logging

from typing import Optional


def divide(a: int, b: int) -> Optional[float]:
    """
    Divide two numbers represented as integers and handle errors gracefully.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        Optional[float]: The result of the division if successful, None otherwise.
        - Returns None if division by zero occurs.
    """
    try:
        return a / b
    except ZeroDivisionError:
        logging.error('Error: Division by zero is not allowed.')
        return None


if __name__ == '__main__':
    # Configure logging to display error messages
    logging.basicConfig(level=logging.INFO)

    # Test 1: Division by zero
    result = divide(22, 0)
    if result is not None:
        print(result)
    else:
        print('Division could not be performed. (Test 1: Division by zero)')

    # Test 2: Successful division
    result = divide(10, 2)
    if result is not None:
        print(f'Successful division: {result}')
    else:
        print('Division could not be performed. (Test 2: Successful division)')