#!/usr/bin/python3
"""read module"""


import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        return f.write(json.dumps(my_obj))
