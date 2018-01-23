import unittest
from Tocka import Tocka
from Segment import Segment
from Poligon import Poligon
from Poligon import nalazenjeKonveksnogOmotaca
from Poligon import konstruirajProstPoligon
from Triangulacije import Sve_moguce_triangulacije,Strukture


class TestTocka (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.t1 = Tocka(0, 0)
        self.t2 = Tocka(1, 0)
        self.t3 = Tocka(1, 1)

    def tearDown(self):
        pass

    def test_orjentacija(self):
        self.assertEqual(self.t1.orjentacija(self.t2,self.t3), 1)
        self.assertEqual(self.t1.orjentacija(self.t3, self.t2), -1)
        self.assertEqual(self.t1.orjentacija(self.t2, self.t1), 0)
        self.assertEqual(self.t1.orjentacija(self.t1, self.t1), 0)

class TestSegment (unittest.TestCase):
            @classmethod
            def setUpClass(cls):
                pass

            @classmethod
            def tearDownClass(cls):
                pass

            def setUp(self):
                self.segment1 = Segment(Tocka(0, 0), Tocka(5, 5))
                self.segment_sijece1 = Segment(Tocka(0, 5), Tocka(5, 0))
                self.segment_ne_sijece1 = Segment(Tocka(-5,-8), Tocka(9, -3))
                self.segment_jedna_zajednicka_tocka = Segment(Tocka(5, 5), Tocka(9, 3))
                self.segment_poklapa_se = Segment(Tocka(0, 0), Tocka(5, 5))
                self.segment_sadrzi1 = Segment(Tocka(0, 0), Tocka(6, 6))
                self.segment_deg = Segment(Tocka(3, 3), Tocka(3, 3))
                self.segment_deg2 = Segment(Tocka(9, 5), Tocka(9, 5))

            def tearDown(self):
                pass

            def test_presjek(self):
                self.assertEqual(self.segment1.provjera_presjeka(self.segment_sijece1), 1)
                self.assertEqual(self.segment1.provjera_presjeka(self.segment_ne_sijece1), 0)
                self.assertEqual(self.segment1.provjera_presjeka(self.segment_jedna_zajednicka_tocka), 1)
                self.assertEqual(self.segment1.provjera_presjeka(self.segment_poklapa_se), 1)
                self.assertEqual(self.segment1.provjera_presjeka(self.segment_sadrzi1), 1)
                self.assertEqual(self.segment_sadrzi1.provjera_presjeka(self.segment1), 1)
                self.assertEqual(self.segment1.provjera_presjeka(self.segment_deg), 1)
                self.assertEqual(self.segment_deg.provjera_presjeka(self.segment_deg2), 0)


class TestPoligon(unittest.TestCase):

            @classmethod
            def setUpClass(cls):
                pass

            @classmethod
            def tearDownClass(cls):
                pass

            def setUp(self):
                self.tocke = (Tocka(0, 0), Tocka(5, 1), Tocka(3, 2), Tocka(4, 3), Tocka(1, 8))
                self.tocke1 = (Tocka(0, 0), Tocka(1, 8), Tocka(4, 3), Tocka(3, 2), Tocka(5, 1))
                self.tocke2 = (Tocka(0, 0), Tocka(5, 0), Tocka(1, 7), Tocka(0, 4), Tocka(1, 2), Tocka(1, 1),
                               Tocka(0, 1))
                self.tocka_unutar = Tocka(3, 3)
                self.tocka_izvan = Tocka(-1, -1)
                self.tocka_izvan_blizu = Tocka(4, 2)
                self.niz_tocaka_izvan = [self.tocka_izvan, self.tocka_izvan_blizu, Tocka(20, -6), Tocka(-0.1, -0.1),
                                         Tocka(6, 2)]
                self.poligonccw = Poligon(self.tocke)
                self.poligoncw = Poligon(self.tocke1)
                self.poligon_rubni=Poligon(self.tocke2)
                self.tocka_izvan_prodje_kroz_segment = Tocka(0, 2)
                self.t1 = Tocka(1, 1)
                self.t2 = Tocka(4, 4)
                self.t3 = Tocka(3, 5)
                self.t4 = Tocka(6, 0)
                self.t5 = Tocka(2, 2)
                self.t6 = Tocka(0, 0)
                self.t7 = Tocka(1, 4)
                self.lista_tocaka = [self.t1, self.t2, self.t3, self.t4, self.t5, self.t6, self.t7]

            def tearDown(self):
                pass

            def test_orjentacija(self):
                self.assertEqual(self.poligonccw.orjentacija(), -1)
                self.assertEqual(self.poligoncw.orjentacija(), 1)

            def test_tocka_u_poligonu(self):
                for i in range(0,len(self.tocke)-1):
                   self.assertEqual(self.poligonccw.tocka_u_poligonu(self.tocke[i]), 1)

                self.assertEqual(self.poligonccw.tocka_u_poligonu(self.tocka_unutar), 1)
                self.assertEqual(self.poligonccw.tocka_u_poligonu(self.tocka_izvan), 0)
                self.assertEqual(self.poligonccw.tocka_u_poligonu(self.tocka_izvan_blizu), 0)
                self.assertEqual(self.poligonccw.prazan_poligon(self.niz_tocaka_izvan), 1)
                self.assertEqual(self.poligon_rubni.tocka_u_poligonu(self.tocka_izvan_prodje_kroz_segment), 0)

            def test_provjera_presjeka_sa_segmentom(self):
                segment_sijece1 = Segment(Tocka(3, 3), Tocka(4, 2))
                segment_sijece_na_2_mj = Segment(Tocka(4, 2), Tocka(0, 2))
                segment_sijece_vise = Segment(Tocka(4, 0), Tocka(3.5, 8))
                segment_stranica = Segment(Tocka(0, 0), Tocka(5, 1))
                segment_pripada = Segment(Tocka(1, 1), Tocka(2, 2))
                segment_ne_pripada = Segment(Tocka(-1, -1), Tocka(-10, -10))

                self.assertEqual(self.poligonccw.presjek_sa_segmentom(segment_sijece1), 1)
                self.assertEqual(self.poligonccw.presjek_sa_segmentom(segment_sijece_na_2_mj), 1)
                self.assertEqual(self.poligonccw.presjek_sa_segmentom(segment_sijece_vise), 1)
                self.assertEqual(self.poligonccw.presjek_sa_segmentom(segment_stranica), 1)
                self.assertEqual(self.poligonccw.presjek_sa_segmentom(segment_pripada), 0)
                self.assertEqual(self.poligonccw.presjek_sa_segmentom(segment_ne_pripada), 0)

            def test_konveksni_omotac(self):
                omotac = Poligon((self.t6, self.t4, self.t2, self.t3, self.t7))
                self.assertEqual(nalazenjeKonveksnogOmotaca(self.lista_tocaka), omotac)

            def test_prost_poligon(self):
                prost_poligon = Poligon((self.t7, self.t3, self.t2, self.t4, self.t6, self.t1, self.t5))
                self.assertEqual(konstruirajProstPoligon(self.lista_tocaka), prost_poligon)


class TesstTriangulacija (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_triangulacija(self):
        lista_tocaka = [Tocka(0,0), Tocka(1,0), Tocka(1,1), Tocka(0,1)]
        lista_triangulacija1 = [ [Segment(Tocka(0,0),Tocka(1,1))] , [Segment(Tocka(1,0),Tocka(0,1))]]
        Sve_moguce_triangulacije(lista_tocaka)
        self.assertEqual(Strukture.lista_triangulacija,lista_triangulacija1)

if __name__ == '__main__':
    unittest.main()



