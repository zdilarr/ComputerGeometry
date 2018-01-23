from Segment import Segment
from PIL import ImageDraw, Image
from baza import *


class Strukture:
    """
    Struktre za čuvanje liste svih mogućih triangulacije,
    kao i pomoćne liste i skupa dijagonala za njihovo nalaženje.
    """
    lista_triangulacija = []
    lista_dijagonala = []
    skup_dijagonala = set()



def Sve_moguce_triangulacije (lista_tocaka):
    """
    :param lista_tocaka: lista točaka kojim je određen konveksni poligon
    :return: sve moguće triangulacije tog poligona

     Funkcija koja nalazi sve moguće triangulacije konveksnog poligona.
     Neka je n broj zadanih točaka. Krećemo se točkama poligona, po tri,
     počevši od prve tri zadane točke u smjeru ccw. Neka su one T1, T2, T3.
     Uzmemo neka prva dijagonala povezuje T1 i T3. Tada sigurno nijedna
     druga dijagonala te triangulacije nema T2 za kranju točku.Tada T2
     možemo izbaciti iz tog podskupa mogućih triangulacija. Rekurzivno
     pozovemo funkciju nad skupom on n-1 točke.
     Osnova rekurzije: lista se sastoji samo od tri točke
     Nakon što nađemo sve triangulacije tog podskupa, vratimo  T2 u listu
     točaka poligona, i ponavljamo postupak za T1, T2, T3 rotirano za jedno
     mjesto. Postupak je gotov nakon što je T3 bila zadnja točka poligona.
    """


    if len(lista_tocaka) <= 3:
        Strukture.lista_triangulacija.append(list(Strukture.lista_dijagonala))
        return

    prvi = 0
    drugi = 1
    treci = 2

    privremeni_stek = []

    while treci < len(lista_tocaka):

        privremena_tocka = lista_tocaka[drugi]
        privremena_dijagonala = Segment(lista_tocaka[prvi], lista_tocaka[treci])

        if not privremena_dijagonala in Strukture.skup_dijagonala:
            Strukture.skup_dijagonala.add(privremena_dijagonala)
        else:
            prvi = prvi + 1
            drugi = drugi + 1
            treci = treci + 1
            continue

        privremeni_stek.append(privremena_dijagonala)
        Strukture.lista_dijagonala.append(privremena_dijagonala)
        lista_tocaka.pop(drugi)
        Sve_moguce_triangulacije(lista_tocaka)

        Strukture.lista_dijagonala.pop()

        lista_tocaka.insert(drugi, privremena_tocka)

        prvi = prvi + 1
        drugi = drugi + 1
        treci = treci + 1

    for par_tacaka in privremeni_stek:
        Strukture.skup_dijagonala.discard(par_tacaka)

    return




def SpremiTriangulacije(lista_tocaka, sve_moguce_triangulacije, sirina,visina,boja_pozadine,olovka):
    """
    Funkcija kreira sliku svake moguće triangulacije konveksnog poligona i sprema je u izlazni direktorij pod rednim
    brojem kako je nađena.

    :param lista_tocaka: za iscrtavanje konveksnog poligona
    :param sve_moguce_triangulacije:  lista listi dijagonala za iscrtavanje
    :param sirina: sirina slike
    :param visina: visina slike
    :param boja_pozadine:
    :param olovka: boja dijagonala i ivica
    :return:
    """

    indeks = 0
    redni_broj_triangulacije = -1
    indeks_dijagonale = 17

    for k in range (len(sve_moguce_triangulacije)):

        redni_broj_triangulacije = redni_broj_triangulacije + 1
        indeks_dijagonale += len(Strukture.lista_triangulacija[redni_broj_triangulacije])+30

        indeks = indeks + 1
        slika = Image.new("RGB", (sirina, visina), boja_pozadine)
        draw = ImageDraw.Draw(slika)
        for i in range(0, len(lista_tocaka)):
            draw.line([lista_tocaka[i % len(lista_tocaka)].daj_x(), lista_tocaka[i % len(lista_tocaka)].daj_y(),
                       lista_tocaka[(i + 1) % len(lista_tocaka)].daj_x(),
                       lista_tocaka[(i + 1) % len(lista_tocaka)].daj_y()], olovka)

        for j in range(0, len(Strukture.lista_triangulacija[redni_broj_triangulacije])):
            draw.line([
                Strukture.lista_triangulacija[redni_broj_triangulacije][j].daj_t1().daj_x(),
                Strukture.lista_triangulacija[redni_broj_triangulacije][j].daj_t1().daj_y(),
                Strukture.lista_triangulacija[redni_broj_triangulacije][j].daj_t2().daj_x(),
                Strukture.lista_triangulacija[redni_broj_triangulacije][j].daj_t2().daj_y()
            ], olovka)
            indeks_dijagonale = indeks_dijagonale+1
        filename = "Triangulacija" + str(indeks) + ".jpg"
        slika.save('Output_folder/' + filename)

    return


def Spremi_u_bazu(lista_tocaka, sve_moguce_triangulacije):
    """
    Funckija koja sprema triangulacije u bazu.
    :param lista_tocaka:
    :param sve_moguce_triangulacije:
    :return:
    """
    Dijagonala.delete().where(Dijagonala.ID_Triangulacije >= 0).execute()
    Triangulacija.delete().where(Triangulacija.ID_Triangulacije >= 0).execute()
    Tocka.delete().where(Tocka.ID_Tocke >= 0).execute()

    indeks = 0
    redni_broj_triangulacije = -1
    indeks_dijagonale = 17

    for i in range(0, len(lista_tocaka)):
        Spremi_tocku(i + 15, lista_tocaka[i].daj_x(), lista_tocaka[i].daj_y())
        pass

    for k in range(len(sve_moguce_triangulacije)):

        redni_broj_triangulacije = redni_broj_triangulacije + 1
        indeks_dijagonale += len(Strukture.lista_triangulacija[redni_broj_triangulacije]) + 30
        Spremi_Triangulaciju(k + 1)
        indeks = indeks + 1

        for j in range(0, len(Strukture.lista_triangulacija[redni_broj_triangulacije])):
            indeks_dijagonale = indeks_dijagonale + 1
            pocetna_tocka = Tocka.select(Tocka.ID_Tocke).where(
                Tocka.x_koordinata == Strukture.lista_triangulacija[redni_broj_triangulacije][j].daj_t1().daj_x()
                and
                Tocka.y_koordinata == Strukture.lista_triangulacija[redni_broj_triangulacije][j].daj_t1().daj_y()
            ).group_by(Tocka.ID_Tocke).order_by(Tocka.ID_Tocke)

            krajnja_tocka = Tocka.select(Tocka.ID_Tocke).where(
                Tocka.x_koordinata == Strukture.lista_triangulacija[redni_broj_triangulacije][j].daj_t2().daj_x()
                and
                Tocka.y_koordinata == Strukture.lista_triangulacija[redni_broj_triangulacije][j].daj_t2().daj_y()
            )

            id_krajnje_tocke = id_pocetne_tocke = 0
            for t in pocetna_tocka:
                id_pocetne_tocke = t.ID_Tocke

            for t in krajnja_tocka:
                id_krajnje_tocke = t.ID_Tocke

            Spremi_Dijagonalu(indeks_dijagonale, k + 1, id_pocetne_tocke, id_krajnje_tocke)


    return
