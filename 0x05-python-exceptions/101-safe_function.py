#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = None
    try:
        res = fct(*args)
        return res
    except Exception as e:
        print("Exception: {}".format(e.args[0]),  file=sys.stderr)
        return res
