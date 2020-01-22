#!/usr/bin/python3
"""json obj module"""

import json


def to_json_string(my_obj):
    """to json function"""
    obj = json.dumps(my_obj)
    return repr(obj)
