#!/usr/bin/python3
"""read module"""


def append_write(filename="", text=""):
    with open(filename, "w+", encoding="utf-8") as f:
        return f.write(text)
