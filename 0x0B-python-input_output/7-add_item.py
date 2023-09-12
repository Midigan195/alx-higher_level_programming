#!/usr/bin/python3
"""
This script adds commad line arguments to a JSON file.

It loads the Json file with load_from_json_file and updates the list
with save_to_json_file. If the file does not exist a new one is created.
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    args = load_from_json_file("add_item.json")
except FileNotFoundError:
    args = []
args.extend(sys.argv[1:])
save_to_json_file(args, "add_item.json")
