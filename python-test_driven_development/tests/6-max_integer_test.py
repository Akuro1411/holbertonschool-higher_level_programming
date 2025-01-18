#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_0_empty(self):
        self.assertIsNone(max_integer())

    def test_1_max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_2_max_start(self):
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_3_max_middle(self):
        self.assertEqual(max_integer([1, 2, 7, 4]), 7)

    def test_4_type(self):
        arr = [1, 2, 3, 4]
        for element in arr:
            self.assertEqual(type(element), int)


if __name__ == "__main__":
    unittest.main()
