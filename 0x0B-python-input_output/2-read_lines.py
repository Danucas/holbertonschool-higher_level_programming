#!/usr/bin/python3
"""read module"""


def read_lines(filename="", nb_lines=0):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")
        if nb_lines <= 0 or nb_lines > len(lines):
            nb_lines = len(lines) - 1
        for i in range(nb_lines):
            print(lines[i])
