#!/usr/bin/python3
"""Create an square with defined size"""


class Square():
    """Square object
    Attributes:
              attr1 (size): size of square"""

    def area(self):
        """Return the square area"""
        return self.__size ** 2

    @property
    def size(self):
        """return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size value
        Args:
            arg1 (value): the value to be setted"""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """Print the square"""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        """return the position tuple"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the size value
        Args:
            arg1 (value): the value to be setted"""
        msg = "position must be a tuple of 2 positive integers"
        if len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = (value[0], value[1])
                else:
                    raise TypeError(msg)
            else:
                raise TypeError(msg)
        else:
            raise TypeError(msg)

    def __init__(self, size=0, position=(0, 0)):
        """init
        Description: initializes size"""
        self.size = size
        self.position = position
