from Triangulacije import *
from Tocka import Tocka
import math

sirina = 400
visina = 400
boja_pozadine = (255, 255, 255)
olovka = (0, 0, 0)
lista_tocaka= []
broj_tocaka = 8

centar = 200
promjer = 100

for i in range(broj_tocaka):
    lista_tocaka.append(
        Tocka(
            centar + promjer*math.cos((2*math.pi*i)/broj_tocaka),
            centar + promjer*math.sin((2*math.pi*i)/broj_tocaka)
        )
    )



Sve_moguce_triangulacije(lista_tocaka)
"""
Rezultat provjeriti u output folderu
"""
SpremiTriangulacije(lista_tocaka, Strukture.lista_triangulacija, sirina, visina, boja_pozadine, olovka)
"""
Odkomentirati  sljedecu funkciju nakon što je baza kreirana:

Spremi_u_bazu(lista_tocaka, Strukture.lista_triangulacija)
"""

def main():

    if __name__ == "__main__":
        main()


