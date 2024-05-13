#!/usr/bin/python3
def no_c(my_string):
    for letter in my_string:
        if ord(letter) == 99 or ord(letter) == 67:
            letter = ''
