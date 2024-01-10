#!/usr/bin/python3
"""
This script displays your id using github api
"""
import sys
import requests


if __name__ == "__main__":

    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    user_data = response.json()
    user_id = user_data.get('id')
    print(user_id)
