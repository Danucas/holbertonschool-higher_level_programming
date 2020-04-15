#!/usr/bin/python3
"""
Python script to fetch an https request
"""


import requests
import sys


def main():
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    response = requests.post(url, data=values)
    txt = response.text
    print(txt)


if __name__ == '__main__':
   main()
    
