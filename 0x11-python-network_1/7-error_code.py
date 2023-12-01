#!/usr/bin/python3
"""
This script prints the error code of url
"""
import requests
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code < 400:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")
