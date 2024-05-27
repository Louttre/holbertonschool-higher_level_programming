#!/usr/bin/python3
"""
This module provides a function to read and print the content of a file.
"""


def read_file(filename=""):
    """
    This function reads the content of a specified file and prints it to the console.
    """

    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
