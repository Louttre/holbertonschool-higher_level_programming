#!/usr/bin/python3
"""
Returns the JSON representation of an object.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    :param my_obj: The object to be serialized to JSON.
    :return: A JSON string representing the object.
    """

    return json.dumps(my_obj)
