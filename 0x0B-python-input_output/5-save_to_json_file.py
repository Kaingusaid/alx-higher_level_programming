#!/usr/bin/python3
"""Object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an object to a file"""

    with open(filename, 'w') as w:
        w.write(json.dumps(my_obj))
