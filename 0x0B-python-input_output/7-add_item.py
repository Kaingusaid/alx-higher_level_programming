#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then save them to a file.
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    arg_list = load_from_json_file("add_item.json")
except Exception:
    arg_list = []

for element in range(1, len(sys.argv)):
    arg_list.append(sys.argv[element])
save_to_json_file(arg_list, "add_item.json")
