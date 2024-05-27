#!/usr/bin/python3
"""
This module provides a function to read and print the content of a file.
"""


def read_file(filename=""):
    """
    This function reads the content of a specified file and prints it to the console.
    
    :param filename: The name of the file to be read. Defaults to an empty string.
    """
    
    with open(filename, 'r', encoding='UTF-8') as file:
        content = file.read()
        print(content)
