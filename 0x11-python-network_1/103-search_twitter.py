#!/usr/bin/python3
"""
Python script to fetch an https request
"""


import requests
import sys
import base64
import json


def main():
    c_k = sys.argv[1]
    c_s = sys.argv[2]
    b_s = '{}:{}'.format(c_k, c_s)
    ms_bytes = b_s.encode('ascii')
    b64s = base64.b64encode(ms_bytes)
    b64s_f = b64s.decode('ascii') 
    headers = {}
    headers['Authorization'] = 'Basic {}'.format(b64s_f)
    headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
    data = {'grant_type': 'client_credentials'}
    auth_ep = 'https://api.twitter.com/oauth2/token'
    bearrer_token = requests.post(auth_ep, data=data, headers=headers)
    token = bearrer_token.json()['access_token']
    url = "https://api.twitter.com/1.1/search/tweets.json"
    query = {'q': sys.argv[3], 'count': 40}
    headers = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url, params=query, headers=headers)
    past_id = 0
    count = 0
    for t in response.json()['statuses']:
        if count == 5:
            break
        name = t['user']['name']
        id_t = t['id']
        text = t['text']
        if 'retweeted_status' in t:
            name = t['retweeted_status']['user']['name']
            text = t['retweeted_status']['text']
            id_t = t['retweeted_status']['id']
            if str(id_t) == str(past_id):
                print("\033[31m\t\tsame id \033[0m")
                continue
        print('[{}] {} by {}'.format(id_t, text, name))
        past_id = id_t
        count += 1


if __name__ == '__main__':
   main()
    
