#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_to_integer = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0
    if not roman_string or len(roman_string) == 0:
        return res
    for i in range(len(roman_string)):
        if i + 1 == len(roman_string) or roman_to_integer[roman_string[i]] >= roman_to_integer[roman_string[i + 1]]:
            res += roman_to_integer[roman_string[i]]
        else:
            res -= roman_to_integer[roman_string[i]]
    return res
