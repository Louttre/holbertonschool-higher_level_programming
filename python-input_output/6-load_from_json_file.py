#!/usr/bin/python3
"""function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Load a JSON-formatted object from a file."""
    with open(filename, "r") as file:
        return json.load(file)
