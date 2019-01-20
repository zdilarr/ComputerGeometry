"""
    Unit tests for Segment class.
    Author: Emilija Zdilar  24-01-2018
"""
import unittest

from point import Point
from segment import Segment


class TestSegment (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.segment1 = Segment(Point(0, 0), Point(5, 5))
        self.segment_intersects1 = Segment(Point(0, 5), Point(5, 0))
        self.segment_does_not_intersect1 = Segment(Point(-5, -8), Point(9, -3))
        self.segment_single_common_endpoint = Segment(Point(5, 5), Point(9, 3))
        self.segment_coincident = Segment(Point(0, 0), Point(5, 5))
        self.segment_contains1 = Segment(Point(0, 0), Point(6, 6))
        self.segment_deg = Segment(Point(3, 3), Point(3, 3))
        self.segment_deg2 = Segment(Point(9, 5), Point(9, 5))

    def tearDown(self):
        pass

    def test_intersection(self):
        self.assertEqual(self.segment1.check_for_intersection(self.segment_intersects1), 1)
        self.assertEqual(self.segment1.check_for_intersection(self.segment_does_not_intersect1), 0)
        self.assertEqual(self.segment1.check_for_intersection(self.segment_single_common_endpoint), 1)
        self.assertEqual(self.segment1.check_for_intersection(self.segment_coincident), 1)
        self.assertEqual(self.segment1.check_for_intersection(self.segment_contains1), 1)
        self.assertEqual(self.segment_contains1.check_for_intersection(self.segment1), 1)
        self.assertEqual(self.segment1.check_for_intersection(self.segment_deg), 1)
        self.assertEqual(self.segment_deg.check_for_intersection(self.segment_deg2), 0)
