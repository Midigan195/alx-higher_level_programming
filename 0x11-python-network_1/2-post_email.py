#!/usr/bin/python3
"""
This script prints the request id of url
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        decoded_response = response.read().decode('utf-8')
        print(decoded_response)
