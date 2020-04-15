#!/usr/bin/python3
"""
Python script to fetch an https request
"""


import requests
import sys


def main():
    url = "https://api.github.com/user"
    data = (sys.argv[1], sys.argv[2])
    response = requests.get(url, auth=data)
    js = response.json()
    if 'id' in js:
        print('{}'.format(js['id']))
    else:
        print('None')

if __name__ == '__main__':
    main()
