import logging

from typing import Optional

# Configure logging at module level
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def divide(a: int, b: int) -> Optional[float]:
    """
    Divide two numbers represented as integers and handle errors gracefully.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        Optional[float]: The result of the division if successful, None otherwise.

    Note:
        Currently only handles ZeroDivisionError. Other exceptions like TypeError
        (if non-integer values are passed) will propagate upwards.
    """

    try:
        return a / b
    except ZeroDivisionError:
        logger.error('Error: Division by zero is not allowed.')
        return None

if __name__ == '__main__':
    # Test 1: Division by zero
    result_divide_by_zero = divide(22, 0)
    if result_divide_by_zero is not None:
        print(result_divide_by_zero)
    else:
        print('Division could not be performed (test 1: division by zero)')

    # Test 2: Successful division
    result_successful_division = divide(10, 2)
    if result_successful_division is not None:
        print(result_successful_division)
    else:
        print('Division could not be performed (test 2: successful division)')