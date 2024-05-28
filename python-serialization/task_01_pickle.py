#!/usr/bin/env python3
import json
import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def __str__(self):
        return "Name: {}\nAge: {}\nIs Student: {}".format(self.name, self.age, self.is_student)

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.__init__, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            loadata = CustomObject()
            with open(filename, rb) as file:
                loadata = pickle.load(filename)
            return loadata
        except (pickle.UnpicklingError, EOFError, Exception):
            return None
