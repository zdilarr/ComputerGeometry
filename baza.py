import peewee
from peewee import *

db = MySQLDatabase('triangulacije', user='root', passwd='')
db.connect()

class Tocka (peewee.Model):
    ID_Tocke = peewee.IntegerField(primary_key=True)
    x_koordinata = peewee.DoubleField(db_column="x_koordinata")
    y_koordinata = peewee.DoubleField(db_column="y_koordinata")
    class Meta:
        database = db

class Triangulacija (peewee.Model):
    ID_Triangulacije = peewee.IntegerField(primary_key=True)
    class Meta:
        database = db


class Dijagonala (peewee.Model):
    ID_Dijagonale = peewee.IntegerField(primary_key=True)
    ID_Triangulacije = peewee.IntegerField(db_column="ID_Triangulacije")
    ID_Pocetne_Tocke = peewee.IntegerField(db_column="ID_Pocetne_Tocke")
    ID_Krajnje_Tocke = peewee.IntegerField(db_column="ID_Krajnje_Tocke")
    class Meta:
        database = db


def Spremi_tocku(PK, x, y):
    Tocka.create(ID_Tocke=PK, x_koordinata=x, y_koordinata=y)


def Spremi_Triangulaciju(PK):
    Triangulacija.create(ID_Triangulacije=PK)


def Spremi_Dijagonalu(PK, ID_Triangulacije, ID_Pocetne_Tocke, ID_Krajnje_Tocke):
    Dijagonala.create(ID_Dijagonale=PK, ID_Triangulacije=ID_Triangulacije, ID_Pocetne_Tocke=ID_Pocetne_Tocke,
                      ID_Krajnje_Tocke=ID_Krajnje_Tocke)
