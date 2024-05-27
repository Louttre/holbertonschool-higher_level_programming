#!/usr/bin/python3
"""
returns an object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    returns an object represented by a JSON string.

    :param my_obj: The object to be serialized to JSON.
    :return: A JSON string representing the object.
    """

    return json.loads(my_str)
