#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([3, 4, 5]), 5)
        self.assertEqual(max_integer([3.8, 4.3, 5.2]), 5.2)
        self.assertEqual(max_integer([-2, -9, -69]), -2)
        self.assertEqual(max_integer([2, 2, 2]), 2)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([0, 3, 3]), 3)
        res = [1, 2, 3, 4, 5, 900, 34, 45, 67, 865, 90, 38, 40]
        self.assertEqual(max_integer(res), 900)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
