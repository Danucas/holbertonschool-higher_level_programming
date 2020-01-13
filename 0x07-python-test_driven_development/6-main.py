#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
try:
    print(max_integer([1, 2, 0x3b76, 4]))
except Exception as e:
    print(type(e).__name__, e)
