#!/usr/bin/python3
"""
This script prints the request id of url
"""
import requests
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
