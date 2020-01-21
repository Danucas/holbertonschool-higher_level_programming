#!/usr/bin/python3
"""read module"""


def number_of_lines(filename=""):
    with open(filename, "r") as f:
        lines = len(f.read().split("\n"))
        return lines
