#!/usr/bin/python3
def magic_string():
    magic_string.c = 1 if not "c" in dir(magic_string) else magic_string.c + 1
    return "".join(["Holberton{}".format(", " if i != magic_string.c - 1 else "") for i in range(magic_string.c)])
