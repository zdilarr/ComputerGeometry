from math import *

class Tocka(object):
    """
    Klasa za točke u ravni. Točka je određena svojom
    x i y koordinatom.
    """
    def __init__(self, x1, y1):
        """
        self - instanca samog objekta, mora se eksplicitno navesti
        __init__ igra ulogu kontruktora, kad deklariramo Tocka()
        python kreira objekt i proslijedi ga init metodi kao parametar
        """
        self.x = x1
        self.y = y1

    def pomjeri_se(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        """
        pretvara objekt u string - t= Tocka... print(t)
        """
        return "Tocka(%s,%s)" % (self.x, self.y)

    def __eq__(self, other):
        """
        Dvije točke su jednake ako su im i x i y koordinate iste
        :param other: točka s kojom poredimo
        :return: 1 ako su jednake, 0 u suprotnom
        """
        return self.x == other.x and self.y == other.y

    def __xor__(self, other):
        if self.x == other.x and self.y == other.y:
            return 0
        return 1

    def __hash__(self):
        return hash((self.x, self.y))

    def daj_x(self):
        return self.x

    def daj_y(self):
        return self.y

    def udaljenost(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def orjentacija(self, t2, t3):
        """
        Orjentacija predstavlja geometrijski zapis koji opisuje odnos točaka u ravni.
        Pri tome je važan poredak kojim su zadane. t1,t2,t3 su orjentirane CCW ako se t3 nalazi
        s lijeve strane duži t1t2. Ideja je da posmatramo znak površine paralelograma razapetog nad
        vektorima t1t2 i t2t3, tj vektorski proizvod t1t2 X t2t3 = k * znak. Posmatramo kojeg je znaka
        varijabla znak.
        :param t2: Tocka
        :param t3: Tocka
        :return: -1 za CCW orjentaciju, 1 za CW orjentaciju, 0 ako su točke kolinearne
        """
        znak = ((t2.daj_x() - self.daj_x()) * (t3.daj_y() - t2.daj_y()) - (t3.daj_x() - t2.daj_x()) *
                (t2.daj_y() - self.daj_y()))
        if znak == 0:
            return 0
        else:
            return -1 if znak < 0 else 1

    def izmedju_tocaka(self, a, b):
        """
        Gledamo orjentaciju tocke koje ispitujemo, dalje u oznaci c, a  i b. Ako tocke nisu kolinearne,
        onda sigurno nije izmedju.
        Ako su kolinearne, gledamo vektore AC I AB, ako su suprotnog smjera C nije izmedju AB.
        Ako su istog smjera posmatramo koji je vektor dulji. Ako je AB dulji od AC, C je izmedju AB.
        U suprotnom, C nije izmedju.
        :param a: prva tocka
        :param b: druga tocka
        :return: 1 ako je izmedju, 0 u suprotnom
        """
        if self.orjentacija(a, b) != 0:
            return 0

        skalarni_p = \
            (self.daj_x()-a.daj_x()) * (b.daj_x() - a.daj_x()) +(self.daj_y() - a.daj_y()) * (b.daj_y() - a.daj_y())
        if skalarni_p < 0:
            return 0

        if (b.daj_x() - a.daj_x()) ** 2 + (b.daj_y()-a.daj_y()) ** 2 < skalarni_p:
            return 0
        return 1
