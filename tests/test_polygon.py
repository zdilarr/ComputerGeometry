"""
    Unit tests for Polygon class.
    Author: Emilija Zdilar  24-01-2018
"""
import unittest

from point import Point
from polygon import Polygon
from polygon import finding_convex_hull
from polygon import simple_polygon_construction
from segment import Segment


class TestPolygon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.points = (Point(0, 0), Point(5, 1), Point(3, 2), Point(4, 3), Point(1, 8))
        self.points1 = (Point(0, 0), Point(1, 8), Point(4, 3), Point(3, 2), Point(5, 1))
        self.points2 = (Point(0, 0), Point(5, 0), Point(1, 7), Point(0, 4), Point(1, 2), Point(1, 1),
                        Point(0, 1))
        self.point_inside = Point(3, 3)
        self.point_outside = Point(-1, -1)
        self.point_outside_near = Point(4, 2)
        self.list_of_points_outside = [self.point_outside, self.point_outside_near, Point(20, -6), Point(-0.1, -0.1),
                                       Point(6, 2)]
        self.polygon_ccw = Polygon(self.points)
        self.polygon_cw = Polygon(self.points1)
        self.polygon_edge = Polygon(self.points2)
        self.point_outside_through_line_segment = Point(0, 2)
        self.t1 = Point(1, 1)
        self.t2 = Point(4, 4)
        self.t3 = Point(3, 5)
        self.t4 = Point(6, 0)
        self.t5 = Point(2, 2)
        self.t6 = Point(0, 0)
        self.t7 = Point(1, 4)
        self.list_of_points = [self.t1, self.t2, self.t3, self.t4, self.t5, self.t6, self.t7]

    def tearDown(self):
        pass

    def test_orientation(self):
        self.assertEqual(self.polygon_ccw.orientation(), -1)
        self.assertEqual(self.polygon_cw.orientation(), 1)

    def test_point_in_polygon(self):
        for i in range(0, len(self.points) - 1):
            self.assertEqual(self.polygon_ccw.point_in_polygon(self.points[i]), 1)

        self.assertEqual(self.polygon_ccw.point_in_polygon(self.point_inside), 1)
        self.assertEqual(self.polygon_ccw.point_in_polygon(self.point_outside), 0)
        self.assertEqual(self.polygon_ccw.point_in_polygon(self.point_outside_near), 0)
        self.assertEqual(self.polygon_ccw.empty_polygon(self.list_of_points_outside), 1)
        self.assertEqual(self.polygon_edge.point_in_polygon(self.point_outside_through_line_segment), 0)

    def test_intersection_with_line_segment(self):
        segment_intersects1 = Segment(Point(3, 3), Point(4, 2))
        segment_intersects_twice = Segment(Point(4, 2), Point(0, 2))
        segment_multiple_intersects = Segment(Point(4, 0), Point(3.5, 8))
        segment_edge = Segment(Point(0, 0), Point(5, 1))
        segment_contained = Segment(Point(1, 1), Point(2, 2))
        segment_not_contained = Segment(Point(-1, -1), Point(-10, -10))

        self.assertEqual(self.polygon_ccw.line_segment_intersection(segment_intersects1), 1)
        self.assertEqual(self.polygon_ccw.line_segment_intersection(segment_intersects_twice), 1)
        self.assertEqual(self.polygon_ccw.line_segment_intersection(segment_multiple_intersects), 1)
        self.assertEqual(self.polygon_ccw.line_segment_intersection(segment_edge), 1)
        self.assertEqual(self.polygon_ccw.line_segment_intersection(segment_contained), 0)
        self.assertEqual(self.polygon_ccw.line_segment_intersection(segment_not_contained), 0)

    def test_convex_hull(self):
        hull = Polygon((self.t6, self.t4, self.t2, self.t3, self.t7))
        self.assertEqual(finding_convex_hull(self.list_of_points), hull)

    def test_simple_polygon(self):
        simple_polygon = Polygon((self.t7, self.t3, self.t2, self.t4, self.t6, self.t1, self.t5))
        self.assertEqual(simple_polygon_construction(self.list_of_points), simple_polygon)
