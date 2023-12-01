#!/usr/bin/python3
"""
This script fetches the response of a url
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print(f"    - type: {type(response.content)}")
    print(f"    - content: {response.text}")
