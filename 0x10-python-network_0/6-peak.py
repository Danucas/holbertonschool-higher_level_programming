#!/usr/bin/python3
"""
Finds a peak in a list
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list
    """
    if not list_of_integers:
        return None
    return rec(list_of_integers, 0, len(list_of_integers) - 1,
               len(list_of_integers))


def rec(l, lw, hg, n):
    """
    recursive algo
    """
    m = lw + (hg - lw) // 2
    if (m == 0 or l[m - 1] <= l[m]) and\
       (m == n - 1 or l[m + 1] <= l[m]):
        return l[m]
    elif (m > 0 and l[m - 1] > l[m]):
        return rec(l, lw, m - 1, n)
    else:
        return rec(l, m + 1, hg, n)
