"""
Contains class for line segment in XY plane.
Author: Emilija Zdilar 24-01-2018
"""
from __future__ import annotations
import point


class Segment (object):
    """
    Class for line segment in plane. Every line segment is determined by its two (distinct)
    endpoints, and it contains all points in between two endpoints, including two endpoints.
    The special case is empty line segment. It is determined by a single endpoint, and it is
    used for edge cases handling.

    """
    def __init__(self, endpoint_t1: point, endpoint_t2: point) -> None:
        self.endpoint_t1 = endpoint_t1
        self.endpoint_t2 = endpoint_t2

    def __str__(self) -> str:
        return "Line segment determined by: (%s,%s)" % (self.endpoint_t1, self.endpoint_t2)

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: Segment) -> bool:
        """
        Two line segments are equal if their endpoints are equal
        Args:
            other: line segment

        Returns: True if they are equal, False otherwise

        """
        return self.endpoint_t1 == other.endpoint_t1 and self.endpoint_t2 == other.endpoint_t2

    def __hash__(self) -> hash:
        return hash((self.endpoint_t1, self.endpoint_t2))

    def return_t1(self) -> point:
        return self.endpoint_t1

    def return_t2(self) -> point:
        return self.endpoint_t2

    def check_for_intersection(self, segment2: Segment) -> int:
        """
        We look at several cases:
        Case 1 - two empty line segments. In that case,  they intersect if they are equal, otherwise not
        Case 2 - two segments that share endpoints intersect (AB and BA intersect, too)
        Case 3 - Let us note two segments with AB and CD. We calculate four orientations ABC, ABD, CDA
                 and CDB. We look at two cases:
                 Case 3.1 - No collinear points. In that case if the first and second pair or orientations
                 are different, line segments intersect. Otherwise, they do not intersect.
                 Case 3.2 - If there are collinear points, we check if one of the segment endpoints lies
                 between the second line segment endpoints. If the answer is yes, line segments intersect.
                 Otherwise, they do not intersect.
        Args:
            segment2: line segment

        Returns: 1 if they intersect, 0 otherwise
        """
        segment3 = Segment(self.return_t2(), self.return_t1())
        if self.return_t1() == self.return_t2():
            if segment2.return_t1() == segment2.return_t2():
                if self == segment2:
                    return 1
                else:
                    return 0
            else:
                return segment2.check_for_intersection(self)

        if self == segment2:
            return 1
        elif segment3 == segment2:
            return 1
        else:
            orj1 = self.endpoint_t1.orientation(self.endpoint_t2, segment2.return_t1())
            orj2 = self.endpoint_t1.orientation(self.endpoint_t2, segment2.return_t2())
            orj3 = segment2.return_t1().orientation(segment2.return_t2(), self.endpoint_t1)
            orj4 = segment2.return_t1().orientation(segment2.return_t2(), self.endpoint_t2)

            if orj1 == 0 or orj2 == 0 or orj3 == 0 or orj4 == 0:
                if segment2.return_t1().between_points(self.endpoint_t1, self.endpoint_t2) or \
                       segment2.return_t2().between_points(self.endpoint_t1, self.endpoint_t2):
                    return 1
                else:
                    return 0

            elif orj1 != orj2 and orj3 != orj4:
                return 1
            else:
                return 0
