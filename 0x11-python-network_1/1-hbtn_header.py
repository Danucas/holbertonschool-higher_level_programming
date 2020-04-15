#!/usr/bin/python3
"""
Python script to fetch an https request
"""


import urllib.request
import sys


def main():
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])


if __name__ == '__main__':
    main()
