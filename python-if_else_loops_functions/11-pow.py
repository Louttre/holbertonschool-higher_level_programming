#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b == 1:
        return a
    if b == 0:
        return result
    if b > 0:
        for i in range(b):
            result *= a
    else:
        for i in range(-b):
            result /= a
    return result
