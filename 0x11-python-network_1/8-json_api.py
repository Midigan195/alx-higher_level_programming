#!/usr/bin/python3
"""
This script sends a post request with a parameter
"""
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    data = {'q': q}
    response = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        json_data = response.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
