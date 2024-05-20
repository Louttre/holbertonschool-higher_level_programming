#!/usr/bin/python3
"""
Adds two integers.

Args:
    a (int, float): The first number.
    b (int, float): The second number, defaults to 98.

Returns:
    int: The sum of a and b, as integers.

Raises:
    TypeError: If either of a or b are not integers or floats.
"""
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

