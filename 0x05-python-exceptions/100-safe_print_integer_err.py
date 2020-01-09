#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError as e:
        print("Exception: {}".format(e.args[0]), file=sys.stderr)
        return False
    except ValueError as e:
        print("Exception: {}".format(e.args[0]), file=sys.stderr)
        return False
