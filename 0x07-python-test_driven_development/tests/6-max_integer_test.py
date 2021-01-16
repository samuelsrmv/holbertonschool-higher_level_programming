#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test max integer to list
    """

    def test_max_in_the_middle(self):
        """tests standard operation"""
        test_list = [1, 2, 99, 3, 4]
        self.assertEqual(max_integer(test_list), 99)

    def test_max_at_the_end(self):
        """standard operation: max is at the end"""
        test_list = [1, 2, 3, 4, 99]
        self.assertEqual(max_integer(test_list), 99)

    def test_max_at_the_beginning(self):
        """standard operation: max is at the beginning"""
        test_list = [99, 1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 99)

    def test_max_one_negative(self):
        """standard operation: list containing one negative value"""
        test_list = [-99, 1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)

    def test_max_all_negative(self):
        """standard operation: list containing all negative values"""
        test_list = [-99, -1, -2, -3, -4]
        self.assertEqual(max_integer(test_list), -1)

    def test_max_one_element(self):
        """standard operation: list containing only one element"""
        test_list = [99]
        self.assertEqual(max_integer(test_list), 99)

    def test_arg_empty_list(self):
        """tests empty list argument"""
        self.assertIs(max_integer([]), None)

    def test_arg_noargs(self):
        """test no arguments"""
        self.assertIs(max_integer(), None)

    def test_error(self):
        """test string"""
        result = max_integer("sad")
        self.assertRaises(Exception, result)

    def test_2(self):
        """test list with string"""
        result = max_integer(["hola"])
        self.assertRaises(Exception, result)

    def test_3(self):
        """test tuple"""
        result = max_integer((2, 3))
        self.assertRaises(TypeError, result)

    def test_4(self):
        """test structure"""
        result = max_integer({})
        self.assertRaises(Exception, result)

    def test_5(self):
        """test no list with None"""
        result = max_integer([None])
        self.assertRaises(Exception, result)
