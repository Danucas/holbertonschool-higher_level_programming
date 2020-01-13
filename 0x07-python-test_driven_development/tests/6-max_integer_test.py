#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test Max integer Class"""
    def test_none(self):
        """Test a None object value"""
        mesg = "object of type 'NoneType' has no len()"
        with self.assertRaisesRegex(TypeError, mesg) as ex:
            max_integer(None)

    def test_none_value(self):
        """Test a None value inside the list"""
        with self.assertRaises(TypeError) as ex:
            max_integer([1, 2, None, 4])

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer(), None)

    def test_non_integer(self):
        """Test a list with a non integer value"""
        with self.assertRaises(TypeError) as ex:
            max_integer([1, 2, "tres", 4])

    def test_hexa_value(self):
        """Test an Hexadecimal value in the list"""
        self.assertEqual(max_integer([1, 2, 0x3b76, 4]), 15222)

    def test_wrong_types(self):
        """Test wrong arguments"""
        with self.assertRaises(TypeError) as ex:
            max_integer(45)
