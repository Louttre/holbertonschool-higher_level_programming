#!/usr/bin/python3
"""module for inherits_from"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherits from a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance of a subclass of the specified class, False otherwise.
    """
    
    return issubclass(type(obj), a_class) and type(obj) != a_class
