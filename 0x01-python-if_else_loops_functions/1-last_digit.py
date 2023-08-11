#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
checknum = number % 10
if number < 0:
    checknum = checknum - 10
if checknum > 5:
    print(f"Last digit of {number} is {checknum} and is greater than 5")
elif checknum == 0:
    print(f"Last digit of {number} is {checknum} and is 0")
elif checknum < 6 and checknum != 0:
    print(f"Last digit of {number} is {checknum} and is less than 6 and not 0")
