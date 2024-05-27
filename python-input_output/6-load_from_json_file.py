#!/usr/bin/python3
"""module with function to append string to file"""
import json


def load_from_json_file(filename):
    """Save the JSON string representation of object to file"""
    with open(filename, "r") as file:
        return json.load(file)
