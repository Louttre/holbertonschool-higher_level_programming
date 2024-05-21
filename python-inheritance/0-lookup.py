#!/usr/bin/python3
"""Module that return a list of attribute of an object"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the attributes and methods.
    """
    return dir(obj)
