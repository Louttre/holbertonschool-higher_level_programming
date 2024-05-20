#!/usr/bin/python3
"""
Print the text with 2 new lines after '.', '?', and ':'.
"""    

def text_indentation(text):
    """
    Print the text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    formatted_text = ""
    for char in text:
        formatted_text += char
        if char in ['.', '?', ':']:
            print("{}\n\n".format(formatted_text.strip()))
            formatted_text = ""
    print("{}".format(formatted_text.strip()))
