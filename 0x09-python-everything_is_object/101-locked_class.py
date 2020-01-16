#!/usr/bin/python3
"""Locked Class module"""


class LockedClass:
    """Locked Class object"""
    def __setattr__(self, attr, value):
        """overwriting set_attr to check the input"""
        if attr != "first_name":
            err = "'" + str(type(self).__name__)
            err += "' object has no attribute '" + attr + "'"
            raise AttributeError(err)
        else:
            self.__dict__[attr] = value
