#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer function"""
    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, 1, 3, 12, 17]), 17)
        self.assertEqual(max_integer([1, 2, 4, 10]), 10)
        self.assertEqual(max_integer([5, 7, 15, 17]), 17)
        self.assertEqual(max_integer([7, 11, 13, 15]), 15)
        self.assertEqual(max_integer([6, 12, 16, 18]), 18)
        self.assertEqual(max_integer([-2, -3, -1]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-9, -3, 3, 8]), 8)
        self.assertEqual(max_integer([8.3, 8.4, 8.5, 8.6]), 8.6)
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)
        self.assertEqual(max_integer([-10, -6, -4, -1]), -1)
