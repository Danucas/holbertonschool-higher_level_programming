#!/usr/bin/python3
"""Square unittest module"""


import unittest
import sys
import os
import json
from models.square import Square


class TestSquare(unittest.TestCase):
    """square test class"""
    def setUp(self):
        """config function"""
        self.sq = Square(1)

    def test_square(self):
        """test simple initialization"""
        self.sq = Square(1)
        self.assertEqual(type(self.sq), Square)

    def test_squa_two(self):
        """test simple initialization two"""
        self.sq = Square(1, 2)
        self.assertEqual(type(self.sq), Square)

    def test_sq_three(self):
        """test simple initialization two"""
        self.sq = Square(1, 2, 3)
        self.assertEqual(type(self.sq), Square)

    def test_bad_par_1(self):
        """test simple initialization"""
        with self.assertRaises(TypeError):
            self.sq = Square("1")

    def test_bad_par_2(self):
        """test simple initialization"""
        with self.assertRaises(TypeError):
            self.sq = Square(1, "2")

    def test_bad_par_3(self):
        """test simple initialization"""
        with self.assertRaises(TypeError):
            self.sq = Square(1, 2, "3")

    def test_bad_par_4(self):
        """test simple initialization"""
        self.sq = Square(1, 2, 3, 4)
        self.assertEqual(type(self.sq), Square)

    def test_neg_par_1(self):
        """test simple initialization"""
        with self.assertRaises(ValueError):
            self.sq = Square(-1)

    def test_neg_par_2(self):
        """test simple initialization"""
        with self.assertRaises(ValueError):
            self.sq = Square(1, -2)

    def test_neg_par_3(self):
        """test simple initialization"""
        with self.assertRaises(ValueError):
            self.sq = Square(1, 2, -3)

    def test_zero_1(self):
        """test simple initialization"""
        with self.assertRaises(ValueError):
            self.sq = Square(0)

    def test_str(self):
        """test simple initialization"""
        self.assertTrue(str(self.sq)[:8] == "[Square]")

    def test_str_exists(self):
        """str exists?"""
        self.assertTrue("__str__" in dir(self.sq))

    def test_to_dictionary(self):
        """to dic"""
        dic = self.sq.to_dictionary()
        self.assertTrue(type(dic) == dict)

    def test_update(self):
        """update test"""
        self.assertTrue("update" in dir(self.sq))

    def test_update_1(self):
        """update test"""
        self.sq.update(89)
        self.assertEqual(self.sq.id, 89)

    def test_update_2(self):
        """update test"""
        self.sq.update(89, 1)
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.id, 89)

    def test_update_3(self):
        """update test"""
        self.sq.update(89, 1, 2)
        self.assertEqual(self.sq.x, 2)
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.id, 89)

    def test_update_4(self):
        """update test"""
        self.sq.update(89, 1, 2, 3)
        self.assertEqual(self.sq.y, 3)
        self.assertEqual(self.sq.x, 2)
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.id, 89)

    def test_update_kwargs(self):
        """update test"""
        self.sq.update(**{'id': 89})
        self.assertEqual(self.sq.id, 89)

    def test_update_kwargs_1(self):
        """update test"""
        self.sq.update(**{'id': 89, 'size': 1})
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.id, 89)

    def test_update_kwargs_2(self):
        """update test"""
        self.sq.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(self.sq.x, 2)
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.id, 89)

    def test_update_kwargs_3(self):
        """update test"""
        self.sq.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(self.sq.y, 3)
        self.assertEqual(self.sq.x, 2)
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.id, 89)

    def test_create_1(self):
        """create testing"""
        self.sq = Square.create(**{'id': 89})
        self.assertEqual(type(self.sq), Square)
        self.assertEqual(self.sq.id, 89)

    def test_create_2(self):
        """create testing"""
        self.sq = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(type(self.sq), Square)
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.id, 89)

    def test_create_3(self):
        """create testing"""
        self.sq = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(type(self.sq), Square)
        self.assertEqual(self.sq.x, 2)
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.id, 89)

    def test_create_4(self):
        """create testing"""
        self.sq = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(type(self.sq), Square)
        self.assertEqual(self.sq.y, 3)
        self.assertEqual(self.sq.x, 2)
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.id, 89)

    def test_save_to_file_1(self):
        """save to file testing"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            txt = f.read()
            self.assertEqual(txt, "[]")

    def test_save_to_file_2(self):
        """save to file testing"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            txt = f.read()
            self.assertEqual(txt, "[]")

    def test_save_to_file_3(self):
        """save to file testing"""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            txt = f.read()
            obj = json.loads(txt)
            self.assertEqual(type(obj), list)
            self.assertEqual(type(obj[0]), dict)

    def test_load_from_file(self):
        """load from file"""
        self.sq = Square.load_from_file()
        self.assertEqual(type(self.sq[0]), Square)

    def test_load_from_file_1(self):
        """load from file"""
        os.remove("Square.json")
        self.sq = Square.load_from_file()
        self.assertEqual(self.sq, [])
