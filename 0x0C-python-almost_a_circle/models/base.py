#!/usr/bin/python3
"""Module Base implementation"""


import json
#import turtle
import time
import random


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
        if list_dictionaries is None:
            return "[]"
        res = json.dumps(list_dictionaries)
        return res

    @classmethod
    def save_to_file(cls, list_objs):
        """parse to json an write the value on a file"""
        string = "[]"
        if list_objs is not None:
            dics = [di.to_dictionary() for di in list_objs]
            string = cls.to_json_string(dics)
        with open(cls.__name__ + ".json", "w") as file:
            file.write(string)

    @staticmethod
    def from_json_string(json_string):
        """return objects list from json string"""
        lis = []
        if json_string is not None:
            lis = json.loads(json_string)
        return lis

    @classmethod
    def create(cls, **dictionary):
        """create function"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """load a pyhton object list from json file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                objs = cls.from_json_string(file.read())
                instances = []
                for obj in objs:
                    inst = cls.create(**obj)
                    instances.append(inst)
                return instances
        except:
            return []

    """@staticmethod
    def draw(list_rectangles, list_squares):
        """#turtle drawing function"""
    """
        colors = ["#C14242", "#f0e746", "#b5ed87", "#87edbc", "#87ede8"]
        colors.append("#eb4034")
        colors.append("#e82ca3")
        colors.append("#1445e3")
        turt = turtle
        lists = list_rectangles + list_squares

        for rect in lists:
            rn = random.randrange(len(colors))
            turt.penup()
            turt.fillcolor(colors[rn])
            turt.pencolor(colors[rn])
            turt.setx(rect.x)
            turt.sety(rect.y)
            turt.seth(0)
            turt.pendown()
            turt.begin_fill()
            turt.forward(rect.width)
            turt.right(90)
            turt.forward(rect.height)
            turt.right(90)
            turt.forward(rect.width)
            turt.right(90)
            turt.forward(rect.height)
            turt.end_fill()
        turt.exitonclick()"""

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save objs as csv files"""
        if cls.__name__ == "Rectangle":
            head = "id,width,height,x,y"
        elif cls.__name__ == "Square":
            head = "id,size,x,y"
        s_obj = ""
        for obj in list_objs:
            obj = obj.to_dictionary()
            attrs = head.split(",")
            s_obj += ",".join([str(obj[key]) for key in attrs])
            s_obj += "\n"
        string = "\n".join([head, s_obj])
            
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            f.write(string)

    @classmethod
    def load_from_file_csv(cls):
        """load objs from csv files"""
        name = cls.__name__
        with open(name + ".csv", "r") as f:
            cont = f.read().split("\n")
            objs =[]
            for obj in cont[1:-1]:
                objs.append(obj.split(","))
            rects = []
            for obj in objs:
                if name == "Rectangle":
                    attrs = ["id", "width", "height", "x", "y"]
                elif name == "Square":
                    attrs = ["id", "size", "x", "y"]
                dic = {key: int(obj[i].strip()) for i, key in enumerate(attrs)}
                rects.append(cls.create(**dic))
            return rects
                
                
    
            
            
