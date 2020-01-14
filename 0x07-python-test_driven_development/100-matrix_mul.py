#!/usr/bin/python3
"""Dot product Module"""


def max_integer(list=[]):
        """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
        """
        if len(list) == 0:
            return None
        result = list[0]
        i = 1
        while i < len(list):
            if list[i] > result:
                result = list[i]
            i += 1
        return result


def matrix_mul(m_a, m_b):
    """matrix multiplication module"""
    if type(m_a) is not list:
        print("TypeError(m_a must be a list)")
    if type(m_b) is not list:
        print("TypeError(m_b must be a list)")

    width, height = len(m_b[0]), len(m_a)
    new_matrix = []
    for y in range(height):
        new_matrix.append([])
        for x in range(width):
            close = False
            res = 0
            for Yn in range(width):
                try:
                    res += m_a[y][Yn] * m_b[Yn][x]
                except Exception as e:
                    print(type(e).__name__, e)
                    close = True
                    break
            if close is True:
                raise ValueError("m_a and m_b can't be multiplied")
            new_matrix[y].append(res)
    return new_matrix
