#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) <= 122 and ord(letter) >= 97:
            print((chr(ord(letter) - 32)), end='')
        else:
            print(letter, end='')
