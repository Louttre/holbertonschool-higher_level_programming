#!/usr/bin/python3
def uppercase(str):
    newlett = ""
    for letter in str:
        if ord(letter) <= 122 and ord(letter) >= 97:
            newlett += chr(ord(letter) - 32)
        else:
            newlett += letter
    print(f"{newlett}\n", end ='')
