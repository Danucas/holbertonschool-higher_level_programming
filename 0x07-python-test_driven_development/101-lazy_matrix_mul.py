#!/usr/bin/python3
"""Lazy mul module"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Lazy numpy matrix dot product"""
    A = np.array(m_a)
    B = np.array(m_b)
    return A.dot(B)
