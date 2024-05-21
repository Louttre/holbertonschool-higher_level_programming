#!/usr/bin/python3
"""
Module for is_same_class function
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
