#!/usr/bin/python3
"""square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init function"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value
        self.__size = value

    def __str__(self):
        """return string representation of square"""
        ret = "[{}] ({}) ".format(type(self).__name__, self.id)
        ret += "{}/{} - {}".format(self.x, self.y, self.size)
        return ret

    def update(self, *args, **kwargs):
        """update attributes function"""
        attrs = ["id", "size", "x", "y"]
        argus = list(args)
        if len(argus) > 0:
            for i, ar in enumerate(argus):
                setattr(self, attrs[i], argus[i])
        else:
            for arg in kwargs.items():
                setattr(self, arg[0], arg[1])

    def to_dictionary(self):
        """to dictionary"""
        dic = self.__dict__
        attrs = ["id", "size", "x", "y"]
        ret = {x: getattr(self, x) for x in attrs}
        return ret
