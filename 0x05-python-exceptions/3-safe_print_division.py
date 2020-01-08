#!/usr/bin/python3
def safe_print_division(a, b):
        res = None
        try:
                res = a / b
        except Exception as r:
                res = None
                print(type(r).__name__)
        finally:
                print("Inside result: {}".format(res))
                return res
