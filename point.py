"""
Contains class for  2D points in XY plane.
Author: Emilija Zdilar 24-01-2018
"""
from __future__ import annotations
from math import *


class Point(object):
    """
    Class for point in plane. Every point is named by its coordinated of the form of (x, y).
    The first number corresponds to the x-coordinate and the second to the y-coordinate.
    """

    def __init__(self, x1: float, y1: float) -> None:
        self.x = x1
        self.y = y1

    def move(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

    def __str__(self) -> str:
        return "Point(%s,%s)" % (self.x, self.y)

    def __eq__(self, other: Point) -> bool:
        """
        Two points A(x1,y1) and B(x2,y2), where x1=x2 and y1=y2 are equal.
        Args:
            other: point that we compare it to

        Returns: True if they are equal, False otherwise

        """
        return self.x == other.x and self.y == other.y

    def __xor__(self, other: Point) -> int:
        if self.x == other.x and self.y == other.y:
            return 0
        return 1

    def __hash__(self) -> hash:
        return hash((self.x, self.y))

    def return_x(self) -> float:
        return self.x

    def return_y(self) -> float:
        return self.y

    def distance(self, p) -> float:
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def orientation(self, t2: Point, t3: Point) -> int:
        """
        Orientation is the geometric notation that describes the relationship between the
        points in the plane. Thereby, the order of points is important. Orientation of an
        ordered triplet of points in the plane can be  either counterclockwise, clockwise
        or collinear. The ordered triplet of points t1,t2,t3 are oriented CCW if t3 is on
        the left side of the line determined by t1 and t2.  The idea is to check the sign
        of the area of the parallelogram spanned by two vectors t1 t2 and t2 t3, i.e. The
        cross product t1t2 X t2t3 = k * sign.
        Args:
            t2: second point
            t3: third point

        Returns:

        """
        sign = ((t2.return_x() - self.return_x()) * (t3.return_y() - t2.return_y()) - (t3.return_x() - t2.return_x()) *
                (t2.return_y() - self.return_y()))
        if sign == 0:
            return 0
        else:
            return -1 if sign < 0 else 1

    def between_points(self, a: Point, b: Point) -> int:
        """
        Method that checks if the given point is between two other points, a and b.  If the
        three points are not collinear, the point does not lie in the middle. Otherwise, we
        look at two vectors AC and AB. If they are not in the same direction, the point does
        not lie in the middle. If they are in the same direction, we check the length of two
        vectors. If AB has greater length than AC, point lies in the middle. Otherwise, the
        point does not lie in the middle.

        Args:
            a: point A
            b: point B

        Returns: 1 if point lies between A and B, 0 otherwise
        """
        if self.orientation(a, b) != 0:
            return 0

        scalar_product = \
            (self.return_x() - a.return_x()) * (b.return_x() - a.return_x()) + \
            (self.return_y() - a.return_y()) * (b.return_y() - a.return_y())
        if scalar_product < 0:
            return 0

        if (b.return_x() - a.return_x()) ** 2 + (b.return_y() - a.return_y()) ** 2 < scalar_product:
            return 0
        return 1
