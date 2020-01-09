#!/usr/bin/python3
"""Create an square with defined size"""
class Square():
    """Square object"""
    def __init__(self, size=0):
        """init
        Description: initializes size"""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
