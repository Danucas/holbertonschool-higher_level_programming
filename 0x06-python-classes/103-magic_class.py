#!/usr/bin/python3
"""magic_module"""

class MagicClass:

    """No lo se"""
    def __init__(self, radius):
        self.__radius=0

        if type (radius) is not int and type (radius) is not float:
            raise TypeError("radius must be a number")
        
        else:
            self.__radius=radius

    def area ():
        return self.__radius**2*math.pi
    
    def circumference():
        return 2*math.pi*self.__radius
