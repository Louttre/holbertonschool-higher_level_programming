#!/usr/bin/python3
"""
Function that writes an Object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves the given Python object to a JSON file.

    Parameters:
    my_obj: Python object to be serialized and written to the file.
    filename (str): The name of the file to which
    the JSON representation will be written.

    Raises:
    IOError: If there is an error writing to the file.
    """

    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj, file))
