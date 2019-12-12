#!/usr/bin/python3
import sys


def main():
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("{} argument:\n{}: {}".format(length - 1, 1, sys.argv[1]))
    else:
        print("{} arguments:".format(length - 1))
        for argc in range(1, length):
            print("{}: {}".format(argc, sys.argv[argc]))


if __name__ == '__main__':
    main()
