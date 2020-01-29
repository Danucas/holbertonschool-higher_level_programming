#!/usr/bin/python3
"""pep8 style test module"""


import unittest
import pep8


class TestStyle(unittest.TestCase):
    """test class"""
    def test_base_style(self):
        """base style checker"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_rect_style(self):
        """rect style checker"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    
