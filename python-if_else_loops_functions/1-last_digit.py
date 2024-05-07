#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
witness = 0
if number < 0:
    number *= -1
    witness = 1
if number % 10 < 6 and number % 10 != 0:
    if witness:
        print(f"Last digit of -{number} is -{number % 10} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {number % 10} and is less than 6 and not 0")
elif number % 10 > 5:
    if witness:
        print(f"Last digit of -{number} is -{number % 10} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {number % 10} and is greater than 5")
else:
    if witness:
        print(f"Last digit of -{number} is -{number % 10} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {number % 10} and is 0")
