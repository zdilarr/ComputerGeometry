"""
    Contains all database models.
    Author: Emilija Zdilar 24-01-2018
"""
import peewee
from peewee import *
from utils.constants import USER, PASSWORD, DB

db = MySQLDatabase(DB, user=USER, passwd=PASSWORD)
db.connect()


class Point (peewee.Model):
    point_id = peewee.IntegerField(primary_key=True)
    x_coordinate = peewee.DoubleField(db_column="x_coordinate")
    y_coordinate = peewee.DoubleField(db_column="y_coordinate")

    class Meta:
        database = db


class Triangulation (peewee.Model):
    triangulation_id = peewee.IntegerField(primary_key=True)

    class Meta:
        database = db


class Diagonal (peewee.Model):
    diagonal_id = peewee.IntegerField(primary_key=True)
    triangulation_id = peewee.IntegerField(db_column="triangulation_id")
    starting_point_id = peewee.IntegerField(db_column="starting_point_id")
    ending_point_id = peewee.IntegerField(db_column="ending_point_id")

    class Meta:
        database = db


def save_point(pk, x, y):
    Point.create(point_id=pk, x_coordinate=x, y_coordinate=y)


def save_triangulation(pk):
    Triangulation.create(triangulation_id=pk)


def save_diagonal(pk, triangulation_id, starting_point_id, ending_point_id):
    Diagonal.create(diagonal_id=pk, triangulation_id=triangulation_id, starting_point_id=starting_point_id,
                    ending_point_id=ending_point_id)
