#!/usr/bin/python3
"""square module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """init function"""
        super().integer_validator("size", size)
        self._Rectangle__width = size
        self._Rectangle__height = size
