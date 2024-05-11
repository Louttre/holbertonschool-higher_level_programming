#!/usr/bin/python3
def uppercase(s):
    result = ""
    for letter in s:
        if ord(letter) >= 97 and ord(letter) <= 122:
            result += f"{chr(ord(letter) - 32)}"
        else:
            result += f"{letter}"
    print("{0}\n".format(result), end='')
