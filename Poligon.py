from Tocka import Tocka
from Segment import Segment
from operator import itemgetter
import math


class Poligon(object):
    """
    Klasa jednostavnog poligona u ravni. Jednostavan poligon je zatvorena kriva u ravni koja nema
    samopresjeka. Poligon je određen uređenom n-torkom 2D točaka, njih nazivamo vrhovi.
    unutarnjih presjeka
    """
    def __init__(self, tocke=()):
        """
        self - instanca samog objekta, mora se eksplicitno navesti
        __init__ igra ulogu kontruktora, kad deklariramo Poligon()
        python kreira objekt i proslijedi ga init metodi kao parametar
        :param tocke: n-torka tocaka
        """
        self.tocke = tocke

    def __str__(self):
        """
        pretvara objekt u string - p = Poligon... print(P)
        :return: string
        """
        niz_tocaka=''
        for i in range(len(self.tocke)):
            niz_tocaka += str(self.tocke[i])
            niz_tocaka += " "
        return "Poligon odredjen: %s" % niz_tocaka

    def __eq__(self, other):
        """
        Dva poligona su jednaka ako su im n-torke točaka iste, s tim da ne moraju počinjati od istog indeksa,
        ali da poredak mora biti očuvan po mod n.
        Npr (1,2,3,4,5) == (5,1,2,3,4)
        :param other: poligon s kojim poredimo
        :return: 1 ako su jednaki, 0 u suprotnom
        """
        if len(self.tocke) != len(other.tocke):
            return 0

        index = -1
        for i in range(0, (len(self.tocke)-1)):
            if self.tocke[i] == other.tocke[0]:
                index = i

        if index == -1:
            return 0

        for i in range(0, (len(self.tocke) - 1)):
            if self.tocke[i] != other.tocke[index]:
                return 0
            else:
                index = (index + 1) % len(self.tocke)
        return 1

    def vrati_tocke(self):
        return self.tocke

    def orjentacija(self):
        """
        Izračunamo površinu jednostavnog poligona, i posmatrajući znak površine određujemo CCW/CW orjentaciju.
        Koristi se poopćena formula od formule za površinu trokuta.
        :return: orjentacija poligona
        """
        suma = 0
        for i in range(len(self.tocke)-1):
            suma += (self.tocke[i+1].daj_x() - self.tocke[i].daj_x())\
                    * (self.tocke[i+1].daj_y() + self.tocke[i].daj_y())
        return -1 if suma < 0 else 1

    def presjek_sa_segmentom(self, segment):
        """
        Provjerava presjek segmenta s poligonom.
        Posmatramo ivice poligona kao segmente, provjerimo presjek svake ivice za zadanim segmentom.
        Čim naiđemo na presjek, odgovor je potvrdan. Smatram da segment ne siječe poligon ako se potpuno nalazi
        izvan ili unutar poligona
        :param segment: segment s kojim provjeravamo presjek
        :return: 1 ako se siječe, 0 u suprotnom
        """
        for i in range(len(self.tocke)):
            stranica = Segment(self.tocke[i], self.tocke[(i+1) % len(self.tocke)])
            if segment.provjera_presjeka(stranica) == 1:
                return 1
        return 0

    def prazan_poligon(self, lista_tocaka):
        """
        Provjera pripada li ijedna točka iz liste poligonu.
        :param lista_tocaka: lista točaka za koju provjeravamo pripada li poligonu
        :return: 1 ako nijedna od točaka nije u poligonu, 0 u suprotnom
        """
        for tocka in lista_tocaka:
            if self.tocka_u_poligonu(tocka) > 0:
                return 0
        return 1

    def tocka_u_poligonu (self, tocka):
        """
        Ideja: Ray Casting
        posmatramo nalazi li se točka na samom rubu, trazeći presjek sa stranicama.
        Pri tome točku posmatramo kao prazan segment. Ako postoji  bar 1 presjek, točka je na rubu poligona.
        Kreiramo segment kojemu je jedna krajnja točka ona koju provjeravamo T, a druga točka T1 sa koordinatama
        (Tx, miny-1). miny je najmanja y koordinata svih točaka poligona.
        Treba nam O(n) vremena da je nađemo i ona imitira zraku.
        Provjerimo presjek sa svakom stranicom poligona, i brojimo presjeke.
        Za ovo nam treba O(n) vremena.
        Prođemo kroz točke poligona i provjeravamo ima li  točaka poligona s istom x-osom i manjom y osom  od točke T.
        Ukoliko nema, vratimo broj presjeka po modulu 2.
        U suprotnom, formiramo listu susjednih vrhova s istom x osom, označimo je sa L. Pri tome pamtimo indeks točaka.
        ( npr. zraka prolazi kroz vrh poligona, taj vrh će biti jedan element liste. npr.
        sadrži cijelu ivicu, dva vrha će biti drugi element liste itd.)
        Specijalno, budući da je poligon zadan kao n-torka točaka, ukoliko su prva i zadnja tocka poligona
        sadržane u zraci, te liste moramo spojiti u jednu.
        (Ako zraka prolazi kroz vrh poligona, broj presjeka je 2, a ako sadrži ivicu, broj presjeka je 3.)
        Oduzmemo od broja presjeka, dužinu svakog elementa liste  L umanjenu za 1.
        Za elemente L, uzmemo prethodnu točku od prve točke liste točaka u listi (zato smo pamtili indeks),
        i sljedeći iza zadnje i gledamo nalaze li se sa suprotnih strana zrake. Ako jesu, umanjimo za 1 broj presjeka.
        Vratimo broj prosjeka po modulu 2

        :param tocka:
        :return:  1 ako je točka u poligonu, 0 u suprotnom
        """
        indeks_minimuma = 0
        broj_presjeka=0
        lista_susjednih=[]

        for i in range(len(self.tocke)):
            if self.tocke[i].daj_y() < self.tocke[indeks_minimuma].daj_y():
                indeks_minimuma = i

        tocka2 = Tocka(tocka.daj_x(), self.tocke[indeks_minimuma].daj_y()-1)
        segment = Segment(tocka, tocka2)

        segment_tocka = Segment(tocka, tocka)

        for i in range(len(self.tocke)):
            stranica = Segment(self.tocke[i], self.tocke[(i + 1) % len(self.tocke)])

            if stranica.provjera_presjeka(segment_tocka) ==1:
                return 1

            elif segment.provjera_presjeka(stranica) == 1:
                broj_presjeka += 1

        susjedni = 0
        for i in range(len(self.tocke)):

            if self.tocke[i].daj_x() == tocka.daj_x() and self.tocke[i].daj_y() <= tocka.daj_y() and susjedni != 1:
                lista_susjednih.append([(self.tocke[i],i)])
                susjedni = 1

            elif self.tocke[i].daj_x() == tocka.daj_x() and self.tocke[i].daj_y() <= tocka.daj_y() and susjedni == 1:
                lista_susjednih[len(lista_susjednih)-1].append((self.tocke[i],i))
                susjedni = 1

            else:
                susjedni = 0

        if not lista_susjednih:
            return broj_presjeka % 2

        if lista_susjednih[0][0][1] == 0 and lista_susjednih[-1][-1][1] == len(self.tocke)-1:
            lista_susjednih[0] = lista_susjednih[-1] + lista_susjednih[0]
            lista_susjednih.pop(-1)
        for i in range(len(lista_susjednih)):
            broj_presjeka -= len(lista_susjednih[i])-1

        for i in range(len(lista_susjednih)):

            prva_tocka=self.tocke[lista_susjednih[i][0][1]-1]

            druga_tocka=self.tocke[ (lista_susjednih[i][(len(lista_susjednih[i])-1)][1]+1)%len(self.tocke)]

            if (tocka.daj_x() - prva_tocka.daj_x()) * (druga_tocka.daj_x()-tocka.daj_x()) >0:
                broj_presjeka -= 1

        return broj_presjeka % 2


def nalazenjeKonveksnogOmotaca(P):
        """
        Konveksni omotač je najmanji zatvoreni konveksni poligon koji sadrži sve tačke koje određuju poligon P.
        Koristim monotone chain algoritam. Sortiramo točke po x (ako su iste onda i po y koordinati).
        pol_1 i pol_2 su gornja i donja polovica konveksnog omotača. Za gornju polovicu idemo od prve dvije točke prema
        zadnjoj i dodajemo  sljedeću točku poligona. Dokle god zadnje tri točke nisu orjentirane CW skidamo zadnju
        točku. Slično za donju polovicu. Spojimo donju i gornju polovicu nakon što uklonimo prvi i zadnji element
        donje polovice da se elementi ne bi ponovili. Rezultat je konveksni omotač

        :param P: Poligon
        :return: konveksni omotač
        """

        if len(P) == 0:
            return
        if len(P) == 1:
            return [P[0]]

        P.sort(key=lambda Tocka: (Tocka.daj_x(), Tocka.daj_y()))

        pol_1 = [P[0], P[1]]
        for i in range(2,len(P)):
            pol_1.append(P[i])
            while len(pol_1) > 2 and not bool(pol_1[-1].orjentacija(pol_1[-2],pol_1[-3])-1):
                del pol_1[-2]

        pol_2 = [P[-1], P[-2]]

        for i in range(len(P)-3,-1,-1):
            pol_2.append(P[i])

            while len(pol_2) > 2 and not bool(pol_2[-1].orjentacija(pol_2[-2],pol_2[-3])-1):
                del pol_2[-2]


        del pol_2[0]
        del pol_2[-1]

        lista_tocaka =  tuple (pol_1  + pol_2)
        konveksni_omotac = Poligon(lista_tocaka)
        return konveksni_omotac


def konstruirajProstPoligon (tocke):
    """
    Konstrukcija jednostavnog poligona od zadanog skupa točaka.
    Ideja je da te točke orjentiramo tj. nađemo centroid poligona i sortiramo kut koji zaklapaju dužine čije su krajnje
    točke (Cx,Cy) i točke poligona te pozitivni dio x-ose, pri tom pamteći u listi indeks točaka poligona.
    Redoslijed je niz indeksa. Kreiramo listu točaka po novom redoslijedu. Tada uređena n-torka tako poredanih
    točaka određuje jednostavan  poligon.
    :param tocke: skup točaka
    :return: jednostavan poligon
    """
    x_koord = []
    y_koord = []

    for i in range(len(tocke)):
        x_koord.append(tocke[i].daj_x())
        y_koord.append(tocke[i].daj_y())

    sum1 = 0
    for i in range(len(x_koord)):
        sum1 += x_koord[i]
    sum2 = 0
    for i in range(len(y_koord)):
        sum2 += y_koord[i]

    cx = float(sum1) / max(len(x_koord), 1)
    cy = float(sum2) / max(len(y_koord), 1)

    a = []
    for i in range(len(x_koord)):
        a.append((math.atan2(y_koord[i] - cy, x_koord[i] - cx), i))
    a.sort(key=itemgetter(0), reverse=True)

    redoslijed = [x[1] for x in a]
    lista_tocaka = []
    for i in range(len(redoslijed)):
        lista_tocaka.append(Tocka(x_koord[redoslijed[i]], y_koord[redoslijed[i]]))
    tuple_tocaka = tuple(lista_tocaka)
    poligon = Poligon(tuple_tocaka)
    return poligon

