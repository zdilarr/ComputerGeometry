"""
    Unit tests for Point class.
    Author: Emilija Zdilar  24-01-2018
"""
import unittest

from point import Point


class TestPoint (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.t1 = Point(0, 0)
        self.t2 = Point(1, 0)
        self.t3 = Point(1, 1)

    def tearDown(self):
        pass

    def test_orientation(self):
        self.assertEqual(self.t1.orientation(self.t2, self.t3), 1)
        self.assertEqual(self.t1.orientation(self.t3, self.t2), -1)
        self.assertEqual(self.t1.orientation(self.t2, self.t1), 0)
        self.assertEqual(self.t1.orientation(self.t1, self.t1), 0)
