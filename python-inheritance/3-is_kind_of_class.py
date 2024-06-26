#!/usr/bin/python3
"""
Module for is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class or inherited from it.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance of the specified class
        or a subclass of it, False otherwise.
    """

    return isinstance(obj, a_class)
