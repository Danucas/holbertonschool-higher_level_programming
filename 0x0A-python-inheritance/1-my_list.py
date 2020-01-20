#!/usr/bin/python3
"""List inheritance module"""


class MyList(list):
    """LIst inheritance class"""
    def print_sorted(self):
        """sorted printing function"""
        print(sorted(self))
