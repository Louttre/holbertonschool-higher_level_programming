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
for letter in roman_string:
    for key, value in roman_to_integer:
        if letter == key:
            res += value
