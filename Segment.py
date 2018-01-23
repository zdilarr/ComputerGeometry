class Segment (object):

    def __init__(self, krajnja_t1, krajnja_t2):
        """
        Klasa kojom opisujemo segmente u ravni.
        Segment je dio prave određen dvjema (različitim) kranjim točkama koji sadrži
        sve točke između tih dvaju točaka i obje kranje točke.
        Specijalno, prazan segment ima iste krajnje točke i služi samo za provjeru nekih
        rubnih slučajeva
        :param krajnja_t1: krajnja točka
        :param krajnja_t2: krajnja točka
        """
        self.krajnja_t1=krajnja_t1
        self.krajnja_t2=krajnja_t2

    def __str__(self):
        """
        pretvara objekt u string - AB=Segment... print(AB)
        :return: string
        """
        return "Segment odredjen s: (%s,%s)" % (self.krajnja_t1, self.krajnja_t2)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        """
        Dva segmenta su jednaka ako su im kranje točke jednake
        :param other: drugi segment s kojim poredimo
        :return: 1 ako su jednaki, 0 u suprotnom
        """
        return self.krajnja_t1 == other.krajnja_t1 and self.krajnja_t2 == other.krajnja_t2

    def __hash__(self):
        return hash((self.krajnja_t1, self.krajnja_t2))

    def daj_t1(self):
        return self.krajnja_t1

    def daj_t2(self):
        return self.krajnja_t2

    def provjera_presjeka(self, segment2):
        """
        -Specijalno, prvo provjerava jesu li u pitanju 2 prazna segmenta. (Iako oni nikad neće biti
        ovako nasumično zadani, važno je da metoda radi za rubne slučajeve jer se koristi u klasi Poligon.)
        Ako jesu moraju biti identični da bi se sjekli, u suprotnom se ne sijeku.
        -Dalje, ako su dva segmenta ista, sijeku se tj. AB siječe AB i AB siječe BA.
        -Ako nisu prazni ni isti: Označimo prvi segment sa AB i drugi sa CD.
        računamo 4 orjentacije ABC,ABD, CDA,CDB.
        U slučaju da nema kolinearnih točaka:
            ako su prve dvije orjentacije različite, i druge dvije različite, sijeku se segmenti.
            U suprotnom se ne sijeku.
        Ako ima kolinearnih točaka, posmatramo da li se jedna od krajnjih točaka segmenta nalazi
        između krajnjih točaka drugog segmenta. Ako to vrijedi bar za jednu točku, segmenti se sijeku.
        U suprotnom segmenti se ne sijeku.

        :param segment2: segment s kojim provjeravamo presjek
        :return: 1 ako se sijeku, 0 u suprotnom
        """
        segment3 = Segment(self.daj_t2(), self.daj_t1())
        if self.daj_t1() == self.daj_t2():
            if segment2.daj_t1() == segment2.daj_t2():
                if self == segment2:
                    return 1
                else:
                    return 0
            else:
                return segment2.provjera_presjeka(self)

        if self == segment2:
            return 1
        elif segment3 == segment2:
            return 1
        else:
            orj1 = self.krajnja_t1.orjentacija(self.krajnja_t2, segment2.daj_t1())
            orj2 = self.krajnja_t1.orjentacija(self.krajnja_t2, segment2.daj_t2())
            orj3 = segment2.daj_t1().orjentacija(segment2.daj_t2(), self.krajnja_t1)
            orj4 = segment2.daj_t1().orjentacija(segment2.daj_t2(), self.krajnja_t2)

            if orj1 == 0 or orj2 == 0 or orj3 == 0 or orj4 == 0:
                if segment2.daj_t1().izmedju_tocaka(self.krajnja_t1, self.krajnja_t2) or \
                       segment2.daj_t2().izmedju_tocaka(self.krajnja_t1, self.krajnja_t2):
                    return 1
                else:
                    return 0

            elif orj1 != orj2 and orj3 != orj4:
                return 1
            else:
                return 0
