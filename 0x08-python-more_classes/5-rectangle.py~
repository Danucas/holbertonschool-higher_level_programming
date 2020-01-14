#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instance initialization"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter"""
        w, h = self.__width * 2, self.__height * 2
        if w == 0 or h == 0:
            w, h = 0, 0
        return w + h

    def __str__(self):
        """str representation"""
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for y in range(self.__height):
            for x in range(self.__width):
                string += "#"
            if y != (self.__height - 1):
                string += "\n"
        return string

    def __repr__(self):
        """instance representation"""
        return "Rectangle(" + str(self.__width)\
            + "," + str(self.__height) + ")"
