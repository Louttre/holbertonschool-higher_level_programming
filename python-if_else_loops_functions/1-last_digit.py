#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
witness = 0
if number < 0:
    number *= -1
    witness = 1
d = number % 10
if d < 6 and d != 0:
    if witness:
        print(f"Last digit of -{number} is -{d} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {d} and is less than 6 and not 0")
elif number % 10 > 5:
    if witness:
        print(f"Last digit of -{number} is -{d} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {d} and is greater than 5")
else:
    if witness:
        print(f"Last digit of -{number} is -{d} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {d} and is 0")
