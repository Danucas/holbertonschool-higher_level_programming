#!usr/bin/python3
"""json obj module"""

import json


def from_json_string(my_str):
    """from json function"""
    new_obj = json.loads(my_str)
    return new_obj
