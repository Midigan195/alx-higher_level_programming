#!/usr/bin/python3
"""
This script prints the error code
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            decoded_response = response.read().decode('utf-8')
            print(decoded_response)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
