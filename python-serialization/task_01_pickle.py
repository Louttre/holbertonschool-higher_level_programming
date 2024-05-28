#!/usr/bin/env python3
"""
This script defines a CustomObject class that includes methods for
serializing to and deserializing from a file using the pickle module.
"""

import json
import pickle


class CustomObject:
    """
    A custom class that represents an object
    with a name, age, and student status.
    """
    def __init__(self, name, age, is_student):
        """
        Initializes the CustomObject with
        the given name, age, and student status.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def __str__(self):
        """
        Returns a string representation of the CustomObject.

        Returns:
            str: A formatted string displaying
            the name, age, and student status.
        """
        return "Name: {}\nAge: {}\nIs Studen\
        t: {}".format(self.name, self.age, self.is_student)

    def serialize(self, filename):
        """
        Serializes the CustomObject instance to a file using pickle.

        Args:
            filename (str): The name of the file
            to which the object will be serialized.

        Returns:
            bool: True if serialization is successful, None otherwise.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a CustomObject instance from a file using pickle.

        Args:
            filename (str): The name of the file
            from which the object will be deserialized.

        Returns:
            CustomObject: The deserialized CustomObject
            instance, or None if deserialization fails.
        """
        try:
            loadata = CustomObject()
            with open(filename, "rb") as file:
                loadata = pickle.load(filename)
            return loadata
        except (pickle.UnpicklingError, EOFError, Exception):
            return None
