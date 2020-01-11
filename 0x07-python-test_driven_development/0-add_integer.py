#!/usr/bin/python3
"""add_integer module
a
a
a
a"""


def add_integer(a, b=98):
    """return sum of two integers
    algo mas
    sad"""
    a_stat = True if isinstance(a, int) else isinstance(a, float)
    b_stat = True if isinstance(b, int) else isinstance(b, float)
    if a_stat and b_stat:
        return int(a) + int(b)
    else:
        mess = " must be an integer"
        if a_stat is False:
            mess = "a" + mess
        elif b_stat is False:
            mess = "b" + mess
        raise TypeError(mess)
