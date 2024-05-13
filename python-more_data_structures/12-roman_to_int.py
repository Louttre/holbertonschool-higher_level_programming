#!/usr/bin/python3
def roman_to_int(roman_string):
    tr = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0
    if not isinstance(roman_string, str) or not roman_string:
        return res
    for i in range(len(roman_string)):
        if i + 1 == len(roman_string) or tr[roman_string[i]] >= tr[roman_string[i + 1]]:
            res += tr[roman_string[i]]
        else:
            res -= tr[roman_string[i]]
    return res
