#!/usr/bin/python3
"""
This module provides a function to print a square of a specified size.
"""


def print_square(size):
    """
    Print a square of '#' characters with the specified size.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer or if it's a negative integer.
        ValueError: If size is less than 0.
    """
    
    if not isinstance(size, int) or size < 0:
        raise TypeError("size must be a non-negative integer")
    
    for i in range(size):
        print('#', end='')
        for j in range(size - 1):
            print('#', end='')
        print()
