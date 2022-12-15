from matica import *
from zlomky import *
from vektory import *
from simplexMethod import *
from simplexKomplet import *

from simplexOptiMiklovic import *
from maticaNaZlomok import *
from simplexkaMetody import *

print('---------------------------------------------------------')
print('--------- LINEARNA OPTIMALIZACIA --------- KEVIN MIKLOVIC')
print('---------------------------------------------------------\n')

matica1 = []
matica2 = []

while True:
    print('*** MENU ***\n 1 - Matice\n 2 - Zlomky\n 3 - Vektory\n 4 - Simplex')
    operacia = input("Vyber si z moznosti: #-")
    if operacia.isdigit():
        operacia = int(operacia)
        if operacia == 1:
            print("\n*** MENU - Vytvorenie matic ***")
            print("MATICA A")
            matica1 = vytvorMatica()
            print("MATICA B")
            matica2 = vytvorMatica()
            vypisMatice(matica1, "A")
            vypisMatice(matica2, "B")
            velkostMat2 = zistiVelkostMatice(matica2)
            velkostMat1 = zistiVelkostMatice(matica1)
            print(velkostMat1)
            print(velkostMat2)
            while True:
                print('*** OPERACIA MATIC *** 1 - Spocitanie | 2 - Odcitanie | 3 - Nasobenie | 4 - Naspäť')
                operaciaMatic = input("Co sa ma stat?: #-")
                if operaciaMatic == "1" and velkostMat1 == velkostMat2:
                    vysledok = scitanieMatice(matica1, matica2)
                    vypisMatice(vysledok, "☻☻☻☻☻☻ A + B")
                elif operaciaMatic == "2" and velkostMat1 == velkostMat2:
                    vysledok = odcitanieMatice(matica1, matica2)
                    vypisMatice(vysledok, "☻☻☻☻☻☻ A - B")
                elif operaciaMatic == "3" and len(matica1[0] == len(matica2)):
                    vysledok = sucinMatice(matica1, matica2)
                    vypisMatice(vysledok, "☻☻☻☻☻☻ A * B")
                elif operaciaMatic == "4":
                    break
                else:
                    print("Pre scitanie a odcitanie matic je potrebne aby boli takej istej velkosti!!!\npre nasobenie je potrebne aby pocet riadkov prvej matice sa zhodoval s poctom stlpvoc v druhej")



        elif operacia == 2:
            print("Vytvorenie zlomkov!")
            zlomok1 = vytvorZlomok()
            zlomok2 = vytvorZlomok()

            print(zlomok1)
            while True:
                print("\n*** MENU - Zlomky *** 1 - Spocitanie | 2 - Odcitanie | 3 - Nasobenie | 4 - Delenie | 5 - Naspäť'")
                operaciaZlomky = input("Co sa ma stat?: #-")
                if operaciaZlomky == "1":
                    vysledokZlomky = sucetZlomkov(zlomok1, zlomok2)
                    vypisZlomku(vysledokZlomky)
                elif operaciaZlomky == "2":
                    vysledokZlomky = odcitanieZlomkov(zlomok1, zlomok2)
                    vypisZlomku(vysledokZlomky)
                elif operaciaZlomky == "3":
                    vysledokZlomky = nasobenieZlomkov(zlomok1, zlomok2)
                    vypisZlomku(vysledokZlomky)
                elif operaciaZlomky == "4":
                    vysledokZlomky = delenieZlomkov(zlomok1, zlomok2)
                    vypisZlomku(vysledokZlomky)
                elif operaciaZlomky == "5":
                    break



        elif operacia == 3:
            print("Vytvorenie vektorov")
            vektor1 = vytvorenieVektora("Vektor 1")
            vektor2 = vytvorenieVektora("Vektor 2")
            while True:
                print("\n*** MENU - Vektory *** 1 - Spocitanie | 2 - Odcitanie | 3 - Nasobenie | 4 - Naspäť")
                operaciaVektor = input("Co sa ma stat?: #-")
                if operaciaVektor == "1" and len(vektor1) == len(vektor2):
                    vysledokVektor = sucetVektora(vektor1, vektor2)
                    vypisVektora(vysledokVektor, vektor1, vektor2, "Vysledok po scitani: \n")
                elif operaciaVektor == "2" and len(vektor1) == len(vektor2):
                    vysledokVektor = odcitanieVektora(vektor1, vektor2)
                    vypisVektora(vysledokVektor, vektor1, vektor2, "Vysledok po odcitani: \n")
                elif operaciaVektor == "3" and len(vektor1) == len(vektor2):
                    vysledokVektor = nasobenieVektora(vektor1, vektor2)
                    vypisVektora(vysledokVektor,vektor1,vektor2, "Vysledok po nasobeni: \n")
                elif operaciaVektor == "4":
                    break
                else:
                    print("vektory nemaju rovnaku dlžku!!!")

        elif operacia == 4:
            print("▬▬▬▬ SIMPLEXOVA METODA ▬▬▬▬")
            simlexM()
        else:
            print("Zadaj prosim spravnu hodnotu!\n")
    else:
        print("Zadaj prosim spravnu hodnotu!\n")

