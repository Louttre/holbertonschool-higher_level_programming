#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Saves the given Python object to a JSON file.
    """

    with open(filename, "w") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Load a JSON-formatted object from a file."""
    with open(filename, "r") as file:
        return json.load(file)
