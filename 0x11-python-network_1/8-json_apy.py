#!/usr/bin/python3
"""
Python script to fetch an https request
"""


import requests
import sys


def main():
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        query = ""
    else:
        query = sys.argv[1]
    values = {'q': query}
    response = requests.post(url, data=values)
    try:
        js = response.json()
        if 'id' in js and 'name' in js:
            print('[{}] {}'.format(js['id'], js['name']))
        else:
            print('No result')
    except:
        print('Not a valid JSON')


if __name__ == '__main__':
    main()
