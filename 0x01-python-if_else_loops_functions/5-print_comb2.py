#!/usr/bin/python3
for i in range(0, 100):
    print("{:0>2d}{per}".format(i, per=", " if i < 99 else "\n"), end='')
