#!/usr/bin/python3
"""read module"""


def number_of_lines(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        lines = len(f.read().split("\n")) - 1
        return lines
