# This script demonstrates a simple division operation with proper error handling.


def divide(a: str, b: str) -> float:
    """
    Divide two numbers represented as strings and handle errors gracefully.

    Args:
        a (str): The numerator as a string.
        b (str): The denominator as a string.

    Returns:
        float: The result of the division if successful, None otherwise.
    """

    try:
        # Ensure inputs are integers
        num_a = int(a)
        num_b = int(b)

        # Check for zero division error explicitly
        if num_b == 0:
            raise ValueError('Denominator cannot be zero.')

        # Perform division
        return num_a / num_b

    except ValueError as e:
        raise ValueError(f'Inputs must be numeric strings: {e}')

    except ZeroDivisionError:
        raise ValueError('Cannot divide by zero.')


if __name__ == '__main__':
    try:
        result = divide('22', '0')
        if result is not None:
            print(result)
    except ValueError as e:
        print(f'An error occurred: {e}')
