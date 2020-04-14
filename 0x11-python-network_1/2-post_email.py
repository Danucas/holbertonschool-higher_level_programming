#!/usr/bin/python3
"""
Python script to fetch an https request
"""


import urllib.request
import urllib.parse
import sys


def main():
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read())


if __name__ == '__main__':
   main()
    
