#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for letter in my_string:
        if ord(letter) == 99 or ord(letter) == 67:
            new_str += ''
        else:
            new_str += letter
    return new_str
