#!/usr/bin/python3
"""
This script defines a function to write
a given text to a specified file.
The file is opened in write mode,
ensuring that the text is written in UTF-8 encoding.
"""


def write_file(filename="", text=""):
    """
    Writes the given text to the specified file.
    
    Parameters:
    filename (str): The name of the file to write to.
    text (str): The text to write to the file.
    """
    
    with open(filename, "w+", encodong="utf-8") as file:
        f.write(text)
