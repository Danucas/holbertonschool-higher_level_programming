#!/usr/bin/python3
"""
Python script to fetch an https request
"""


import urllib.request
import urllib.parse
import urllib.error
import sys


def main():
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            txt = response.read()
            charset = response.headers.get_content_charset()
            print(txt.decode(charset))
    except urllib.error.HTTPError as e:
        print(e)


if __name__ == '__main__':
   main()
    
