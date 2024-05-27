#!/usr/bin/python3
import sys
import json


def save_to_json_file(my_obj, filename):
    """
    Saves the given Python object to a JSON file.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    """Load a JSON-formatted object from a file."""
    with open(filename, "r") as file:
        return json.load(file)

try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []
data.extend(sys.argv[1:])
save_to_json_file(data, "add_item.json")
