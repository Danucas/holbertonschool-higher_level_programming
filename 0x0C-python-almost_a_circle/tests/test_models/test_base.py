#!/usr/bin/python3
"""Base unittest module"""


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Base test class"""
    def setUp(self):
        """setup function"""
        self.base = Base(1)

    def test_name(self):
        """testing id assignment"""
        self.assertEqual(self.base.id, 1)

    def test_none_id(self):
        """none id test"""
        test_base = Base(None)
        self.assertEqual(test_base.id, 6)

    def test_multiple_instances(self):
        """test multiple instances"""
        test1 = Base(3)
        test2 = Base(None)
        test3 = Base(None)
        self.assertEqual(test1.id, 3)
        self.assertEqual(test2.id, 4)
        self.assertEqual(test3.id, 5)

    def test_how_many(self):
        """test how many objects has been created"""
        with self.assertRaises(Exception) as e:
            self.to_json_string()
        self.assertEqual(type(e.exception), AttributeError)

    def test_none_dic(self):
        """test None list when convert to json string"""
        dic = Base.to_json_string(None)
        self.assertEqual(dic, "[]")

    def test_empty_dic_list(self):
        """test empty list when convert to json"""
        dic = Base.to_json_string([])
        self.assertEqual(dic, "[]")

    def test_to_json(self):
        """testing to json parsing"""
        dic = [{"id": 2}]
        prub = json.dumps(dic)
        test = Base.to_json_string(dic)
        self.assertEqual(prub, test)

    def test_save_to_file(self):
        """testing saving json string to file"""
        dic = [Rectangle(1, 1), Rectangle(1, 2)]
        text = ""
        Rectangle.save_to_file(dic)
        with open("Rectangle.json", "r") as f:
            text = json.loads(f.read())
        dic = [di.to_dictionary() for di in dic]
        self.assertEqual(json.loads(Base.to_json_string(dic)), text)
    def test_from_json(self):
        """test from json string function"""
        dic = [Rectangle(1, 1).to_dictionary(), Rectangle(1, 2).to_dictionary()]
        inp = Rectangle.to_json_string(dic)
        out = Rectangle.from_json_string(inp)
        self.assertEqual(type(dic), list)
        self.assertEqual(type(inp), str)
        self.assertEqual(type(out), list)

    def test_create(self):
        """Test create and update function"""
        dic = {"id": 4, "width": 2, "height": 2}
        rect = Rectangle.create(**dic)
        self.assertEqual(type(rect), Rectangle)
