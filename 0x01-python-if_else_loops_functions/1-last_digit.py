#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = abs(number) % 10
if number < 0:
    d = -d
    print("Last digit of {} is {} and is ".format(number, d), end="")
if d > 5:
    print("Last digit of {} is greater than 5".format(number)
elif d == 0:
    print("Last digit of 0 is 0 and is 0")
else:
    print("less than 6 and not 0")
