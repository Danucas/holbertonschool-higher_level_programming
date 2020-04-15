#!/usr/bin/python3
"""
Python script to fetch an https request
"""


import urllib.request


def main():
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        txt = response.read()
        charset = response.headers.get_content_charset()
        print('Body response:')
        print('\t- type: {}'.format(type(txt)))
        print('\t- content: {}'.format(txt))
        print('\t- utf8 content: {}'.format(txt.decode(charset)))


if __name__ == '__main__':
    main()
