#!/usr/bin/python3
"""inherits from module"""


def inherits_from(obj, a_class):
    """inherits from function"""
    for base in obj.__class__.__bases__:
        if str(base) == str(a_class):
            return True
        for bas in base.__class__.__bases__:
            if str(bas) == str(a_class):
                return True
    return False
