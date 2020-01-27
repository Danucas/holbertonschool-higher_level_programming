#!/usr/bin/python3
"""Module Base"""


import json


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string"""
        res = json.dumps(list_dictionaries)
        return res

    @classmethod
    def save_to_file(cls, list_objs):
        """parse to json an write the value on a file"""
        if list_objs is not None:
            if all(issubclass(cls, Base) for x in list_objs):
                dics = [di.to_dictionary() for di in list_objs]
                string = cls.to_json_string(dics)
                with open(cls.__name__ + ".json", "w") as file:
                    file.write(string)
