#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = "{}".format(number)
last = int(last[-1])
if number < 0:
    last = last * (-1)
print("Last digit of {:d} is".format(number, last), end=" ")
if last > 5:
    print("{:d} and is greater than 5".format(last))
elif last < 6 and last != 0:
    print("{:d} and is less than 6 and not 0".format(last))
elif last == 0:
    print("{:d} and is 0".format(last))
