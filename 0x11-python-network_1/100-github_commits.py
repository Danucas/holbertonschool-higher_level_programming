#!/usr/bin/python3
"""
Python script to fetch an https request
"""


import requests
import sys


def main():
    url = "https://api.github.com/repos/{}/{}/commits"
    url = url.format(sys.argv[2], sys.argv[1])
    response = requests.get(url)
    commits = response.json()
    for com in commits[:10]:
        sha = com['sha']
        author = com['commit']['author']['name']
        print('{}: {}'.format(sha, author))

if __name__ == '__main__':
    main()
