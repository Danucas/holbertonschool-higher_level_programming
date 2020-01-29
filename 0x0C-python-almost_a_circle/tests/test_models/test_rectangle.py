#!/usr/bin/python3
"""Rectangle unittest module"""


import unittest
import sys
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle test class"""
    def setUp(self):
        """setup rectangle function"""
        self.rect = Rectangle(3, 3)

    def test_load_from_file_2(self):
        """load from file"""
        self.rect.save_to_file([Rectangle(1, 2)])
        self.assertEqual(type(self.rect.load_from_file()[0]), Rectangle)

    def test_save_to_file_rect(self):
        """save to none"""
        self.assertEqual(self.rect.save_to_file([Rectangle(1, 2)]), None)

    def test_load_from_file(self):
        """load from file"""
        os.remove("Rectangle.json")
        self.assertEqual(self.rect.load_from_file(), [])

    def test_save_to_file_empty_list(self):
        """save to none"""
        self.assertEqual(self.rect.save_to_file([]), None)

    def test_save_to_file_none(self):
        """save to none"""
        self.assertEqual(Rectangle.save_to_file(None), None)

    def test_to_dict(self):
        """to dictionary test"""
        dic = self.rect.to_dictionary()
        tes = {'id': 51, 'x': 0, 'height': 3, 'y': 0, 'width': 3}
        self.assertEqual(dic, tes)

    def test_display_exists(self):
        """display exists"""
        self.assertTrue("display" in dir(self.rect))

    def test_str_rect(self):
        """checking __str__"""
        self.rect = Rectangle(2, 2)
        self.assertEqual(str(self.rect), "[Rectangle] (50) 0/0 - 2/2")

    def test_neg_init_zero_2(self):
        """negaitve parameter"""
        with self.assertRaises(ValueError):
            self.rect = Rectangle(1, 0)

    def test_neg_init_zero_1(self):
        """negaitve parameter"""
        with self.assertRaises(ValueError):
            self.rect = Rectangle(0, 2)

    def test_neg_init_4(self):
        """negaitve parameter"""
        with self.assertRaises(ValueError):
            self.rect = Rectangle(1, 2, 3, -4)

    def test_neg_init_3(self):
        """negaitve parameter"""
        with self.assertRaises(ValueError):
            self.rect = Rectangle(1, 2, -3)

    def test_neg_init_2(self):
        """negaitve parameter"""
        with self.assertRaises(ValueError):
            self.rect = Rectangle(1, -2)

    def test_neg_init_1(self):
        """negaitve parameter"""
        with self.assertRaises(ValueError):
            self.rect = Rectangle(-1, 2)

    def test_init_5_args(self):
        """wrong fourth parameter"""
        self.rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(type(self.rect), Rectangle)

    def test_wrong_init_4(self):
        """wrong fourth parameter"""
        with self.assertRaises(TypeError):
            self.rect = Rectangle(1, 2, 3, "4")

    def test_wrong_init_3(self):
        """wrong first parameter"""
        with self.assertRaises(TypeError):
            self.rect = Rectangle(1, 2, "3")

    def test_wrong_init_2(self):
        """wrong first parameter"""
        with self.assertRaises(TypeError):
            self.rect = Rectangle(1, "2")

    def test_wrong_init_1(self):
        """wrong first parameter"""
        with self.assertRaises(TypeError):
            self.rect = Rectangle("1", 2)

    def test_four_args(self):
        """four arguments init"""
        self.rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(type(self.rect), Rectangle)

    def test_four_args(self):
        """four arguments init"""
        self.rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(type(self.rect), Rectangle)

    def test_rect_three_args(self):
        """simple three args rect"""
        self.rect = Rectangle(1, 2, 3)
        self.assertEqual(type(self.rect), Rectangle)

    def test_simple_rectangle(self):
        """simple rectangle"""
        self.rect = Rectangle(1, 2)
        self.assertEqual(type(self.rect), Rectangle)

    def test_change_width_by_negative(self):
        """change width values by negative"""
        with self.assertRaises(ValueError):
            self.rect.width = -1

    def test_change_height_by_negative(self):
        """change height values by negative"""
        with self.assertRaises(ValueError):
            self.rect.height = -1

    def test_change_width_by_zero(self):
        """change width values by zero"""
        with self.assertRaises(ValueError):
            self.rect.height = 0

    def test_change_height_by_zero(self):
        """change height values by zero"""
        with self.assertRaises(ValueError):
            self.rect.height = 0

    def test_width_str(self):
        """try setting a string"""
        with self.assertRaises(TypeError):
            self.rect.width = "s"

    def test_height_str(self):
        """try setting a string"""
        with self.assertRaises(TypeError):
            self.rect.height = "s"

    def test_assign_x_neg(self):
        """assign x in negative"""
        with self.assertRaises(ValueError):
            self.rect.x = -2

    def test_assign_y_neg(self):
        """assign y in negative"""
        with self.assertRaises(ValueError):
            self.rect.y = -2

    def test_get_area(self):
        """get area function"""
        self.assertEqual(self.rect.area(), 9)

    def test_get_area_dif_width(self):
        """get area function"""
        self.rect.width = 8
        self.assertEqual(self.rect.area(), 24)
        self.rect.width = 3

    def test_get_area_dif_height(self):
        """get area function"""
        self.rect.height = 7
        self.assertEqual(self.rect.area(), 21)

    def test_simple_display(self):
        """try display"""
        self.rect.width = 2
        self.rect.height = 2
        sys.stdout = open('out.dat', "w")
        self.rect.display()
        sys.stdout.close()
        text = ""
        with open("out.dat", "r") as f:
            text = f.read()
        prub = "##\n"*2
        self.assertEqual(text, prub)

    def test_display_padding(self):
        """try display padding"""
        self.width = 3
        self.height = 3
        self.rect.x = 2
        self.rect.y = 2
        sys.stdout = open('out.dat', "w")

        self.rect.display()
        sys.stdout.close()
        text = ""
        with open("out.dat", "r") as f:
            text = f.read()
        prub = "\n\n"
        prub += "  ###\n"*3
        self.assertEqual(text, prub)
