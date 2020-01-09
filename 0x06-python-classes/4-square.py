#!/usr/bin/python3
"""Create an square with defined size"""


class Square():
    """Square object
    Attributes:
              attr1 (size): size of square"""
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

    def area(self):
        """Return the square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Return the square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size"""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
