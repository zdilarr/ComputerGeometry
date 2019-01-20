"""
    Unit tests for Triangulation class.
    Author: Emilija Zdilar  24-01-2018
"""
import unittest

from point import Point
from segment import Segment
from triangulations import all_possible_triangulations, Structs


class TestTriangulation (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_triangulation(self):
        list_of_points = [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]
        list_of_triangulations1 = [[Segment(Point(0, 0), Point(1, 1))], [Segment(Point(1, 0), Point(0, 1))]]
        all_possible_triangulations(list_of_points)
        self.assertEqual(Structs.list_of_triangulations, list_of_triangulations1)
