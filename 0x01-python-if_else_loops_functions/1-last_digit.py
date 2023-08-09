#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_num = number

if number >= 0:
    if number == 0 or number % 10 == 0:
        print(f"Last digit of {number:d} is 0 and is 0")
    elif number % 10 > 5:
        print(f"Last digit of {number:d} is {number:d} and is greater than 5")
    else:
        print(f"Last digit of {number:d} is {number:d} and is less than 6 and not 0")

if number < 0:
    abs_num = number * -1
    print(f"Last digit of -{abs_num:d} is -{abs_num:d} and is less than 6 and not 0")
