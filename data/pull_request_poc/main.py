#!/usr/bin/env python
# This script demonstrates a simple division operation with proper error handling.

def divide(a, b):
    try:
        # Ensure inputs are integers
        num_a = int(a)
        num_b = int(b)
        return num_a / num_b
    except ValueError:
        print('Inputs must be numbers.')
        return None
    except ZeroDivisionError:
        print('Cannot divide by zero.')
        return None

if __name__ == '__main__':
    result = divide("22", 0)
    if result is not None:
        print(result)