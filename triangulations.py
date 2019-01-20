from segment import Segment
from PIL import ImageDraw, Image
from models import *
from utils.constants import TRIANGULATION, JPG_EXTENSION, OUTPUT_FOLDER


class Structs:
    """
    Helper lists for keeping the list of all possible triangulations,
    as well as set of diagonals.
    """

    list_of_triangulations = []
    list_of_diagonals = []
    set_of_diagonals = set()


def all_possible_triangulations(list_of_points):
    """
    Method that finds all possible triangulations of a convex polygon. Let
    n be the number of given points. We move around points triple-wise, in
    CCW orientation, starting from the first point - T1, T2, T3. Let the
    first diagonal be between T1 and T3. Then no other diagonals for that
    triangulations have T2 for their endpoint. We exclude T2. Recursive
    call is made for n-1 points. Base case is when we only have three
    points. After finding all triangulations for that subset, we return
    T2 in the list and repeat the procedure after moving up. Algorithm
    stops when T3 is the last point of polygon
    Args:
        list_of_points:

    Returns:

    """
    if len(list_of_points) <= 3:
        Structs.list_of_triangulations.append(list(Structs.list_of_diagonals))
        return

    first = 0
    second = 1
    third = 2

    temp_stack = []

    while third < len(list_of_points):

        temp_point = list_of_points[second]
        temp_diagonal = Segment(list_of_points[first], list_of_points[third])

        if temp_diagonal not in Structs.set_of_diagonals:
            Structs.set_of_diagonals.add(temp_diagonal)
        else:
            first = first + 1
            second = second + 1
            third = third + 1
            continue

        temp_stack.append(temp_diagonal)
        Structs.list_of_diagonals.append(temp_diagonal)
        list_of_points.pop(second)
        all_possible_triangulations(list_of_points)

        Structs.list_of_diagonals.pop()

        list_of_points.insert(second, temp_point)

        first = first + 1
        second = second + 1
        third = third + 1

    for pair_of_points in temp_stack:
        Structs.set_of_diagonals.discard(pair_of_points)

    return


def save_triangulations(list_of_points, all_possible_triangulations_, width, height, bg_color, pen) -> None:
    """
    Method that creates an image of triangulations and saves it to output folder
    Args:
        list_of_points: points
        all_possible_triangulations_: triangulations
        width: image width
        height: image height
        bg_color: background color
        pen: line color

    Returns: None

    """

    index = 0
    triangulation_index = -1
    diagonal_index = 17

    for k in range(len(all_possible_triangulations_)):

        triangulation_index = triangulation_index + 1
        diagonal_index += len(Structs.list_of_triangulations[triangulation_index]) + 30

        index = index + 1
        image = Image.new("RGB", (width, height), bg_color)
        draw = ImageDraw.Draw(image)
        for i in range(0, len(list_of_points)):
            draw.line([list_of_points[i % len(list_of_points)].return_x(), list_of_points[i % len(list_of_points)].
                      return_y(),
                       list_of_points[(i + 1) % len(list_of_points)].return_x(),
                       list_of_points[(i + 1) % len(list_of_points)].return_y()], pen)

        for j in range(0, len(Structs.list_of_triangulations[triangulation_index])):
            draw.line([
                Structs.list_of_triangulations[triangulation_index][j].return_t1().return_x(),
                Structs.list_of_triangulations[triangulation_index][j].return_t1().return_y(),
                Structs.list_of_triangulations[triangulation_index][j].return_t2().return_x(),
                Structs.list_of_triangulations[triangulation_index][j].return_t2().return_y()
            ], pen)
            diagonal_index = diagonal_index+1
        filename = TRIANGULATION + str(index) + JPG_EXTENSION
        image.save(OUTPUT_FOLDER + filename)
    return


def save_to_database(list_of_points, all_possible_triangulations_) -> None:
    """
    Method that saves all triangulations to database
    Args:
        list_of_points: points to be saved to database
        all_possible_triangulations_: list of triangulations

    Returns: None

    """

    Diagonal.delete().where(Diagonal.triangulation_id >= 0).execute()
    Triangulation.delete().where(Triangulation.triangulation_id >= 0).execute()
    Point.delete().where(Point.point_id >= 0).execute()

    index = 0
    triangulation_index = -1
    diagonal_index = 17

    for i in range(0, len(list_of_points)):
        save_point(i + 15, list_of_points[i].return_x(), list_of_points[i].return_y())
        pass

    for k in range(len(all_possible_triangulations_)):

        triangulation_index = triangulation_index + 1
        diagonal_index += len(Structs.list_of_triangulations[triangulation_index]) + 30
        save_triangulation(k + 1)
        index = index + 1

        for j in range(0, len(Structs.list_of_triangulations[triangulation_index])):
            diagonal_index = diagonal_index + 1
            starting_point = Point.select(Point.point_id).where(
                Point.x_coordinate == Structs.list_of_triangulations[triangulation_index][j].return_t1().return_x()
                and
                Point.y_coordinate == Structs.list_of_triangulations[triangulation_index][j].return_t1().return_y()
            ).group_by(Point.point_id).order_by(Point.point_id)

            ending_point = Point.select(Point.point_id).where(
                Point.x_coordinate == Structs.list_of_triangulations[triangulation_index][j].return_t2().return_x()
                and
                Point.y_coordinate == Structs.list_of_triangulations[triangulation_index][j].return_t2().return_y()
            )

            ending_point_id = starting_point_id = 0
            for t in starting_point:
                starting_point_id = t.point_id

            for t in ending_point:
                ending_point_id = t.point_id

            save_diagonal(diagonal_index, k + 1, starting_point_id, ending_point_id)
    return
