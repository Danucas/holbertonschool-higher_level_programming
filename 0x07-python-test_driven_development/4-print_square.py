#!/usr/bin/python3
"""Print square module
"""


def print_square(size):
    """funtion that print a given size square"""
    if isinstance (size, int) and size  < 0:
        raise ValueError ("size must be >= 0")

    if isinstance (size, float) and size < 0:
        raise TypeError ("size must be an integer")

    if isinstance (size, int) or isinstance (size, float):
    
        for i in range (size):
            [print ("#", end="") for i in range (size)]
            print ()
    else:
        raise TypeError("size must be an integer")
