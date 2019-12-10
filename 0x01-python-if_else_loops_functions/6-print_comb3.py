#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            print("{}{}{en}".format(i, j, en=", " if i != 8 else "\n"), end="")
