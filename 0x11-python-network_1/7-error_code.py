#!/usr/bin/python3
"""
Python script to fetch an https request
"""


import requests
import sys


def main():
    url = sys.argv[1]
    response = requests.get(url)
    code = response.status_code
    if code > 400:
        print('Error code: {}'.format(code))
    else:
        print(response.text)

if __name__ == '__main__':
   main()
    
