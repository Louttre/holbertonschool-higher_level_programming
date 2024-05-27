#!/usr/bin/python3
"""
This module provides functionality
to append text to an existing file.
If the file does not exist, it will create a
new one and append the text to it.
The module ensures that the file handling is
done with UTF-8 encoding to support
a wide range of text characters.
"""


def append_write(filename="", text=""):
    """
    Appends the given text to the specified file.

    Opens the file in append mode,
    which allows text to be added to the end of the file
    without truncating it. If the file does not exist,
    it creates a new file.

    Parameters:
    filename (str): The path to the file.
    text (str): The text to be appended to the file.
    """

    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
    return len(text)
