import sys

from maticaNaZlomok import *
from simplexkaMetody import *
#################################################################
########## ↓☺↓ ZADAJ SI SVOJ PRIKLAD DO TABULIEK ↓☺↓ #########
pocetPomocnych_P = 2
pocetPomocnych_U = 2

tabulkaStredNazvy = [["b","x1","x2","p1","p2","u1","u2"]]
tabulkaStred = [[14, 3, 2, 0, 0, 1, 0],
                [2, 2, -4, -1, 0, 0, 1],
                [19, 4, 3, 0, 1, 0, 0],
                [0, 3, 2, 0, 0, 0, 0]]

wTabulka = [[0, 0, 0, 0, 0, 0, 0]]
bazaTabulka = [["nic", "nic", "nic"]]
########## ↑☺↑ ZADAJ SI SVOJ PRIKLAD DO TABULIEK ↑☺↑ #########
#################################################################

pocetRiadkov = len(tabulkaStred)
pocetStlpcov = len(tabulkaStred[0])


print("\n////////////////////////////////////////////////////////////")
print("-------------------- ZACIATOK PROGRAMU --------------------")
print("////////////////////     miklovic      /////////////////////")
print("////////////////////      kevin        /////////////////////")
if (pocetPomocnych_U > 0):
    vynulovane = 0
    # zistenie kolko mame pomocnych a kolko riadkov ideme spocitavat '1'
    pomocnePolePreVypocetW = zistiKolkoRiadkovPre_W(tabulkaStred, pocetPomocnych_P, pocetPomocnych_U, pocetStlpcov, pocetRiadkov)
    # vytvorenie zlomkovych polí
    tabulkaStredZlomkova = spravZlomkovu(tabulkaStred)
    wTabulkaZlomkova = spravZlomkovu(wTabulka)
    # tvorenie 'W' funkcie
    wTabulkaZlomkova = vytvorW(tabulkaStredZlomkova, wTabulkaZlomkova, pocetPomocnych_U, pomocnePolePreVypocetW)
    vypisSimplexky(tabulkaStredZlomkova, wTabulkaZlomkova)
    while vynulovane != 'koniec':
        print(" ------------- POCITAME SIMPLEXKU S POMOCNYMI! ------------------- \n")
        vynulovane = hladanieNulovehoriadkuW(wTabulkaZlomkova, pocetStlpcov, pocetPomocnych_U)
        print("♥♥♥")
        print(vynulovane)
        print("♥♥♥")
        if vynulovane != 'koniec':
            #print(pomocnePolePreVypocetW)
            #print(wTabulkaZlomkova)
            #zisti najvacsie zaporne cislo v cenovej funkcii 'W' -vysledok da poziciu stlpca!
            poziciaNajMinusovehoStlpecPivot = zistiNajvacsieZaporneCislo(wTabulkaZlomkova, pocetStlpcov, pocetPomocnych_U)
            print(wTabulkaZlomkova)
            print(str("\nNAJVACSIE ZAPORNE CISLO V CENOVEJ FUNKCII 'W' je: ")+ str(wTabulkaZlomkova[0][poziciaNajMinusovehoStlpecPivot]))
            print(str("a jeho pozicia ('W') je: ") + str(poziciaNajMinusovehoStlpecPivot) + "\n")
            #prva hodnota je po deleni bazy..  DRUHA je riadok pivota
            poziciaPivotaRiadok = vyberPivota(tabulkaStredZlomkova, poziciaNajMinusovehoStlpecPivot, pocetRiadkov)
            print("\nNas pivot je: "+str(tabulkaStredZlomkova[poziciaPivotaRiadok][poziciaNajMinusovehoStlpecPivot]) + " a jeho pozicia riadka je: " + str(poziciaPivotaRiadok))
            #vydelenie pivotoveho riadku pivotom
            tabulkaStredZlomkova = vydelPivotom(tabulkaStredZlomkova, poziciaPivotaRiadok, poziciaNajMinusovehoStlpecPivot)
            #GCD - najvacsi delitel
            tabulkaStredZlomkova = GCD(tabulkaStredZlomkova, pocetRiadkov, pocetStlpcov)
            #funkcia pre vynulovanie stlpca pod a nad pivotom
            tabulkaStredZlomkova = gaussEliminacnaMetoda(tabulkaStredZlomkova, poziciaPivotaRiadok, poziciaNajMinusovehoStlpecPivot, pocetStlpcov)
            wTabulkaZlomkova = gaussMetodForW(tabulkaStredZlomkova, wTabulkaZlomkova, poziciaPivotaRiadok, poziciaNajMinusovehoStlpecPivot, pocetStlpcov)
            tabulkaStredZlomkova = GCD(tabulkaStredZlomkova, pocetRiadkov, pocetStlpcov)
            vypisSimplexky(tabulkaStredZlomkova, wTabulkaZlomkova)
        elif vynulovane == 'totalnyKoniec':
            print("\n////////// DALEJ SA NEDA POKRACOVAT A TU JE VYSTUP: //////////")
            vypisSimplexky(tabulkaStredZlomkova, wTabulkaZlomkova)
            sys.exit()
        elif vynulovane == 'koniec':
            print("\n\n\nZACIATOK\n\n\n")
            a = 1
            print("SKONCILI SME A NASLI NULOVY VEKTOR ---> IDEME NA KLASICKU SIMPLEXKU")
            tabulkaStredZlomkova = prehodTabulky(tabulkaStredZlomkova, pocetStlpcov, pocetPomocnych_U)

            while a == 1:
                vypisDefaultSimplex(tabulkaStredZlomkova)
                poz = zistenieZapornejSumy(tabulkaStredZlomkova)
                print("Pozicia zapornej hodnoty je pre hladanie pivota: STLPEC - "+str(poz))
                pozPivotaRiadok = hladajPivota(tabulkaStredZlomkova, poz)
                print("\n\n\n")
                tabulkaStredZlomkova = vydelPivotom(tabulkaStredZlomkova, pozPivotaRiadok, poz)
                print("AHOJ")
                vypisDefaultSimplex(tabulkaStredZlomkova)
                tabulkaStredZlomkova = gaussEliminacnaMetoda(tabulkaStredZlomkova, pozPivotaRiadok, poz, pocetStlpcov)
                vypisDefaultSimplex(tabulkaStredZlomkova)
                a = 0

#KLASICKA SIMPLEXKA - POCITANIE
print(" ------------- POCITAME KLASICKU SIMPLEXKU! ------------------- \n")
#zistenieZapornejSumy(tabulkaStredZlomkova)

#TO DO
# 2 - chceme vynulovat cely stlpec pod aj nad pivotom pomocou gausovej
# 3 - ak je 'W' tak ho odstranime prec
# 4 - upravujeme kym neda vysledok a vypiseme

