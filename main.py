#!/usr/bin/env python
# This script demonstrates a simple division operation with error handling.

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Cannot divide by zero.')
        return None

if __name__ == '__main__':
    result = divide(10, 0)
    if result is not None:
        print(result)