#!/usr/bin/python3
"""return class as json serialization compatible"""


def class_to_json(obj):
    """to json parseable function"""
    return obj.__dict__
