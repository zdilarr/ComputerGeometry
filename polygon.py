"""
Contains class for  simple polygon in plane.
Author: Emilija Zdilar 24-01-2018
"""
from __future__ import annotations
from typing import Tuple, Union, List
from point import Point
from segment import Segment
from operator import itemgetter
import math


class Polygon(object):
    """
    Simple polygon in plane. Simple polygon is closed shape consisting of straight,
    non-intersecting line segments that are joined pair-wise to form a closed path.
    Polygon is determined by a tuple of 2D points, called vertices.
    """
    def __init__(self, points=()) -> None:
        self.points = points

    def __str__(self) -> str:
        list_of_points = ''
        for i in range(len(self.points)):
            list_of_points += str(self.points[i])
            list_of_points += " "
        return "Polygon determined by: %s" % list_of_points

    def __eq__(self, other: Polygon) -> int:
        """
        Two simple polygons are equal, if their vertices tuples are the same. Starting index is not
        important, but the order of the points (mod n) is. An example is (1,2,3,4,5) == (5,1,2,3,4)
        Args:
            other: other polygon

        Returns: 1 if why are equal, 0 otherwise

        """
        if len(self.points) != len(other.points):
            return 0

        index = -1
        for i in range(0, (len(self.points) - 1)):
            if self.points[i] == other.points[0]:
                index = i

        if index == -1:
            return 0

        for i in range(0, (len(self.points) - 1)):
            if self.points[i] != other.points[index]:
                return 0
            else:
                index = (index + 1) % len(self.points)
        return 1

    def return_points(self) -> Tuple[Point]:
        return self.points

    def orientation(self) -> int:
        """
        We calculate the area of the simple polygon using generalized formula for calculating
        the area of a triangle. CW/CCW orientation is determined by looking at the sign.
        Returns:

        """
        sum_ = 0
        for i in range(len(self.points) - 1):
            sum_ += (self.points[i + 1].return_x() - self.points[i].return_x())\
                    * (self.points[i + 1].return_y() + self.points[i].return_y())
        return -1 if sum_ < 0 else 1

    def line_segment_intersection(self, segment: Segment) -> int:
        """
        Method that checks for polygon-line segment intersection. We look at the polygon sides
        as line segments. We for intersection for each of the sides. If segment intersects any
        of the polygon sides, the answer is affirmative. If the line segment is completely in-
        side of outside of polygon, the answer is negative.
        Args:
            segment: Segment object

        Returns: 1 if there is intersection, 0 otherwise

        """
        for i in range(len(self.points)):
            edge = Segment(self.points[i], self.points[(i + 1) % len(self.points)])
            if segment.check_for_intersection(edge) == 1:
                return 1
        return 0

    def empty_polygon(self, list_of_points) -> int:
        """
        Method that, for a given list of points, ches if there is a single point
        that belongs to the polygon.
        Args:
            list_of_points:

        Returns: 1 if there is, 0 otherwise

        """
        for point in list_of_points:
            if self.point_in_polygon(point) > 0:
                return 0
        return 1

    def point_in_polygon(self, point: Point) -> int:
        """
        Idea - Ray Casting.
        We check if the point belongs to any of the line segments coincident to polygon sides.
        Point is considered to be an empty line segment in that case. If there exists at least
        a single intersection, the point is on the edge of polygon.
        The ray - We create a line segment determined by point passed through parameter and a
        (Tx, miny-1) point. It takes O(n) to find miny - we are looking for the polygon vertex
        with the smallest value on y axis. We then go through all polygon vertices and check if
        there are any points with same value on x axis and smaller value on y axis than T. When
        there are not, we return number of intersections modulo 2. Otherwise, we form the list
        L of neighbour vertices with same x value on x axis, and we also memorize point index.
        Special case: if the first and list point of polygons are containt in the ray, they need
        to be merged.
        If the ray goest through the edge of the polygon, number of intersections is 3. If the
        ray contains the side of polygon, number of intersections is 3. We subtract the length
        of all elements of L reduced for 1. For elements in L, we take predecessor point from a
        first point in list and successor point from a last element in the list and we check if
        they are on the opposite sides of the ray. If they are, we reduce by one the number of
        intersections.
        We return the number of intersections modulo 2.
        Args:
            point:

        Returns:

        """
        index_minimum = 0
        no_of_intersections = 0
        neighbours_list = []

        for i in range(len(self.points)):
            if self.points[i].return_y() < self.points[index_minimum].return_y():
                index_minimum = i

        point2 = Point(point.return_x(), self.points[index_minimum].return_y() - 1)
        segment = Segment(point, point2)

        segment_point = Segment(point, point)

        for i in range(len(self.points)):
            edge_ = Segment(self.points[i], self.points[(i + 1) % len(self.points)])

            if edge_.check_for_intersection(segment_point) == 1:
                return 1

            elif segment.check_for_intersection(edge_) == 1:
                no_of_intersections += 1

        neighbour_ = 0
        for i in range(len(self.points)):

            if self.points[i].return_x() == point.return_x() and \
                    self.points[i].return_y() <= point.return_y() and neighbour_ != 1:
                neighbours_list.append([(self.points[i], i)])
                neighbour_ = 1

            elif self.points[i].return_x() == point.return_x() and \
                    self.points[i].return_y() <= point.return_y() and neighbour_ == 1:
                neighbours_list[len(neighbours_list)-1].append((self.points[i], i))
                neighbour_ = 1

            else:
                neighbour_ = 0

        if not neighbours_list:
            return no_of_intersections % 2

        if neighbours_list[0][0][1] == 0 and neighbours_list[-1][-1][1] == len(self.points)-1:
            neighbours_list[0] = neighbours_list[-1] + neighbours_list[0]
            neighbours_list.pop(-1)
        for i in range(len(neighbours_list)):
            no_of_intersections -= len(neighbours_list[i])-1

        for i in range(len(neighbours_list)):

            first_point = self.points[neighbours_list[i][0][1] - 1]

            second_point = self.points[(neighbours_list[i][(len(neighbours_list[i]) - 1)][1] + 1) % len(self.points)]

            if (point.return_x() - first_point.return_x()) * (second_point.return_x() - point.return_x()) > 0:
                no_of_intersections -= 1

        return no_of_intersections % 2


def finding_convex_hull(poly) -> Union[None, List[Point], Polygon]:
    """
    Convex hull is the smallest convex polygon that contains all the points that determine polygon
    poly. The idea: monotone chain algorithm. Points are sorted by x (or y if they have same value
    on the x axis). Pol_1 and pol_2 are upper and lower halves of convex hull. For upper half we
    move from first to last point point of polygon, and we add the next point. While the last three
    points are not CW oriented, we remove the last point. Lower half works similarly. We merge the
    two halves after removing first and last element from the upper half. The result is the convex
    hull of the simple polygon.
    Args:
        poly: polygon

    Returns: convex hull

    """

    if len(poly) == 0:
        return
    if len(poly) == 1:
        return [poly[0]]

    poly.sort(key=lambda point: (point.return_x(), point.return_y()))

    pol_1 = [poly[0], poly[1]]
    for i in range(2, len(poly)):
        pol_1.append(poly[i])
        while len(pol_1) > 2 and not bool(pol_1[-1].orientation(pol_1[-2], pol_1[-3]) - 1):
            del pol_1[-2]

    pol_2 = [poly[-1], poly[-2]]

    for i in range(len(poly) - 3, -1, -1):
        pol_2.append(poly[i])

        while len(pol_2) > 2 and not bool(pol_2[-1].orientation(pol_2[-2], pol_2[-3]) - 1):
            del pol_2[-2]

    del pol_2[0]
    del pol_2[-1]

    list_of_points = tuple(pol_1 + pol_2)
    convex_hull = Polygon(list_of_points)
    return convex_hull


def simple_polygon_construction(points):
    """
    Method that constructs simple polygon for a given set of points. The idea is to orient the
    points, i.e. to find the polygon centroid and sort the angles that segments with endpoints
    (Cx, Cy) and polygon vertices form with positive x-axis, while memorizing the index of the
    polygon vertices. The list of indexes represents the new order. A defined tuple determines
    the simple polygon.

    Args:
        points:

    Returns: polygon

    """

    x_coordinate = []
    y_coordinate = []

    for i in range(len(points)):
        x_coordinate.append(points[i].return_x())
        y_coordinate.append(points[i].return_y())

    sum1 = 0
    for i in range(len(x_coordinate)):
        sum1 += x_coordinate[i]
    sum2 = 0
    for i in range(len(y_coordinate)):
        sum2 += y_coordinate[i]

    cx = float(sum1) / max(len(x_coordinate), 1)
    cy = float(sum2) / max(len(y_coordinate), 1)

    a = []
    for i in range(len(x_coordinate)):
        a.append((math.atan2(y_coordinate[i] - cy, x_coordinate[i] - cx), i))
    a.sort(key=itemgetter(0), reverse=True)

    order = [x[1] for x in a]
    points_list = []
    for i in range(len(order)):
        points_list.append(Point(x_coordinate[order[i]], y_coordinate[order[i]]))
    points_tuple = tuple(points_list)
    polygon = Polygon(points_tuple)
    return polygon
