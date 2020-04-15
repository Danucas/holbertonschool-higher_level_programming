#!/usr/bin/python3
"""
Python script to fetch an https request
"""


import requests


def main():
    response = requests.get("https://intranet.hbtn.io/status")
    txt = response.text
    print('Body response:')
    print('\t- type: {}'.format(type(txt)))
    print('\t- content: {}'.format(txt))
    #print('\t- utf8 content: {}'.format(txt.decode(charset)))


if __name__ == '__main__':
   main()
    
