#!/usr/bin/python3
"""read module"""


def append_write(filename="", text=""):
    """append"""
    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)
