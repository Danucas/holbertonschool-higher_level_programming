#!/usr/bin/python3
"""read module"""


import json


def save_to_json_file(my_obj, filename):
    """save json to file"""
    with open(filename, "w") as f:
        return f.write(json.dumps(my_obj))
