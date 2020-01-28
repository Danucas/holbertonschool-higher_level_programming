#!/usr/bin/python3
"""Rectangle unittest module"""


import unittest
import sys
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle test class"""
    def setUp(self):
        """setup rectangle function"""
        self.rect = Rectangle(3, 3)

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
