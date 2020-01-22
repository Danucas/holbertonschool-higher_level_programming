#!/usr/bin/python3
"""read module"""


import json


def load_from_json_file(filename):
    """load from json"""
    with open(filename, "r") as f:
        return json.loads(f.read())
