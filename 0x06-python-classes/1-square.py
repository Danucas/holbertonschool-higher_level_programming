#!/usr/bin/python3
"""Create an square with defined size"""


class Square():
    """Square object"""
    def __init__(self, size=None):
        """init
        Description: initializes size"""
        if size is not None:
            self.__size = size
