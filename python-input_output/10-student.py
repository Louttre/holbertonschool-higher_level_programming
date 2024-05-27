#!/usr/bin/python3
"""Student class."""

class Student:
    """
    Defines a student with first name, last name, and age.
    """
    
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.
        
        :param first_name: The first name of the student.
        :param last_name: The last name of the student.
        :param age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        :param attrs: List of attribute names to retrieve.
        :return: A dictionary containing the specified attributes.
        """
        if attrs is None:
            return vars(self)
        else:
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict
