#!/usr/bin/python3
"""
This module defines a function that creates an object from a json file

This module contains one function that creates an object from a json file
"""
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

with open("add_item.json", 'a') as f:
    args = ["apple", "bannana"]
    save_to_json_file(args, "add_item.json")
