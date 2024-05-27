#!/usr/bin/python3
"""
Module
"""


def class_to_json(obj):
    """
    Returns a dictionary description of an object for JSON serialization.

    :param obj: An instance of a class.
    :return: A dictionary with serializable attributes of the object.
    """

    attributes = obj.__dict__
    serializable_attributes = {}
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[key] = value 
    return serializable_attributes
