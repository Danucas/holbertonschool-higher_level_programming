#!/usr/bin/python3
"""
Python script to fetch an https request
"""


import requests
import sys


def main():
    response = requests.get(sys.argv[1])
    try:
        print(response.headers['X-Request-Id'])
    except:
        pass


if __name__ == '__main__':
    main()
