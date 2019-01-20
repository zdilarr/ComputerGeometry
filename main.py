"""
Contains method call for generating and
saving all triangulations.
Author: Emilija Zdilar 24-01-2018
"""
from triangulations import *
from point import Point
import math
from utils.constants import NO_OF_POINTS, CENTER, DIAMETER, WIDTH, HEIGHT, BG_COLOR, PEN

list_of_points = []

for i in range(NO_OF_POINTS):
    list_of_points.append(
        Point(
            CENTER + DIAMETER * math.cos((2 * math.pi * i) / NO_OF_POINTS),
            CENTER + DIAMETER * math.sin((2 * math.pi * i) / NO_OF_POINTS)
        )
    )


all_possible_triangulations(list_of_points)
save_triangulations(list_of_points, Structs.list_of_triangulations, WIDTH, HEIGHT, BG_COLOR, PEN)
save_to_database(list_of_points, Structs.list_of_triangulations)


def main()-> None:
    if __name__ == "__main__":
        main()
