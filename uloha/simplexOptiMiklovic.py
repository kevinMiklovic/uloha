import sys

from maticaNaZlomok import *
from simplexkaMetody import *
#################################################################
########## ↓☺↓ ZADAJ SI SVOJ PRIKLAD DO TABULIEK ↓☺↓ #########

tabulkaStredNazvy = ["b","x1","x2","p1","p2","u1","u2"]
tabulkaStred = [[14, 3, 2, 0, 0, 1, 0],
                [2, 2, -4, -1, 0, 0, 1],
                [19, 4, 3, 0, 1, 0, 0],
                [0, 3, 2, 0, 0, 0, 0]]

########## ↑☺↑ ZADAJ SI SVOJ PRIKLAD DO TABULIEK ↑☺↑ #########
#################################################################
########## ↓☺↓ ZADAJ SI SVOJ PRIKLAD DO TABULIEK ↓☺↓ #########
"""
tabulkaStredNazvy = [["b","x1","x2","p1","p2"]]
tabulkaStred = [[14, 3, 2, 0, 0,],
                [2, -6, -4, -1, 0,],
                [19, -12, 3, 0, 1,],
                [0, -2, -9, 0, 0,]]
"""
########## ↑☺↑ ZADAJ SI SVOJ PRIKLAD DO TABULIEK ↑☺↑ #########
#################################################################
#pre kazdu simplexku si zadefunijeme a pouzijeme podla nutnosti
pocetPomocnych_P = 2
pocetPomocnych_U = 2    #ak robime zakladnu simplexku tak piseme '0'
wTabulka = [[0, 0, 0, 0, 0, 0, 0]]
bazaTabulka = ["nic", "nic", "nic"]     #nastavujem podla toho kolko mame riadkov

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
        vynulovane = hladanieNulovehoriadkuW(wTabulkaZlomkova, pocetStlpcov, pocetPomocnych_U)
        if vynulovane != 'koniec':
            #print(pomocnePolePreVypocetW)
            #print(wTabulkaZlomkova)
            #zisti najvacsie zaporne cislo v cenovej funkcii 'W' -vysledok da poziciu stlpca!
            poziciaNajMinusovehoStlpecPivot = zistiNajvacsieZaporneCislo(wTabulkaZlomkova, pocetStlpcov, pocetPomocnych_U)
            print(wTabulkaZlomkova)
            print(str("\nNAJVACSIE ZAPORNE CISLO V CENOVEJ FUNKCII 'W' je: ")+ str(wTabulkaZlomkova[0][poziciaNajMinusovehoStlpecPivot]))
            print(str("pivota hladame v cenovej funkcie ('W') - STLPEC: ") + str(poziciaNajMinusovehoStlpecPivot) + "\n")
            #prva hodnota je po deleni bazy..  DRUHA je riadok pivota
            poziciaPivotaRiadok = vyberPivota(tabulkaStredZlomkova, poziciaNajMinusovehoStlpecPivot, pocetRiadkov)
            print("\nNas pivot je: "+str(tabulkaStredZlomkova[poziciaPivotaRiadok][poziciaNajMinusovehoStlpecPivot]) + " a jeho pozicia riadka je: " + str(poziciaPivotaRiadok))
            print(poziciaPivotaRiadok)
            print(poziciaNajMinusovehoStlpecPivot)
            bazaTabulka[poziciaPivotaRiadok] = tabulkaStredNazvy[poziciaNajMinusovehoStlpecPivot+1]
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
            print("\n\n☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼")
            print("☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼ FUNKCIA 'W' bola odstranena ☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼\n")
            a = '1'
            tabulkaStredZlomkova = prehodTabulky(tabulkaStredZlomkova, pocetStlpcov, pocetPomocnych_U)
            pocetRiadkov = len(tabulkaStredZlomkova)
            pocetStlpcov = len(tabulkaStredZlomkova[0])
            print("pocet riadkov: " + str(pocetRiadkov))
            print("pocet stlpcov: "+str(pocetStlpcov))
            vypisDefaultSimplex(tabulkaStredZlomkova)
            while a == '1':
                a = ukoncenie(tabulkaStredZlomkova, pocetStlpcov, pocetRiadkov)
                if a == '0':
                    tabulkaStredZlomkova = GCD(tabulkaStredZlomkova, pocetRiadkov, pocetStlpcov)
                    print()
                    print("Všetky neznáme pre cenovu funkciu: "+str(tabulkaStredNazvy))
                    print("Neznáme v BÁZE: " + str(bazaTabulka))
                    vypisVysledku(tabulkaStredZlomkova, tabulkaStredNazvy)
                    print("\n//////////////////////////////////////////////////////")
                    print("//////////////   KONIEC PROGRAMU   ///////////////////")
                    print("//////////////////////////////////////////////////////")
                    sys.exit()
                poz = zistenieZapornejSumy(tabulkaStredZlomkova)
                pozPivotaRiadok = hladajPivota(tabulkaStredZlomkova, poz)
                print("Pozicia pivota: STLPEC - " + str(poz) + "   RIADOK -  " + str(pozPivotaRiadok) + "  hodnota pivota je: "+ str(tabulkaStredZlomkova[pozPivotaRiadok][poz]))
                print()
                #bazaTabulka[pozPivotaRiadok] = tabulkaStredNazvy[poz]
                tabulkaStredZlomkova = vydelPivotom(tabulkaStredZlomkova, pozPivotaRiadok, poz)
                tabulkaStredZlomkova = GCD(tabulkaStredZlomkova, pocetRiadkov, pocetStlpcov)
                tabulkaStredZlomkova = gaussEliminacnaMetoda(tabulkaStredZlomkova, pozPivotaRiadok, poz, pocetStlpcov)
                tabulkaStredZlomkova = GCD(tabulkaStredZlomkova, pocetRiadkov, pocetStlpcov)
                vypisDefaultSimplex(tabulkaStredZlomkova)
                print("//////////////////////////////// '♦' ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

elif (pocetPomocnych_U == 0):
    tabulkaStredZlomkova = spravZlomkovu(tabulkaStred)
    vypisDefaultSimplex(tabulkaStredZlomkova)
    a = '1'
    while a == '1':
        a = ukoncenie(tabulkaStredZlomkova, pocetStlpcov, pocetRiadkov)
        if a == '0':
            tabulkaStredZlomkova = GCD(tabulkaStredZlomkova, pocetRiadkov, pocetStlpcov)
            print(bazaTabulka)
            print("\n//////////////////////////////////////////////////////")
            print("//////////////   KONIEC PROGRAMU   ///////////////////")
            print("//////////////////////////////////////////////////////")
            sys.exit()
        poz = zistenieZapornejSumy(tabulkaStredZlomkova)
        pozPivotaRiadok = hladajPivota(tabulkaStredZlomkova, poz)
        print("\nPozicia zapornej hodnoty je pre hladanie pivota: STLPEC - " + str(poz) + " a jeho hodnota je: " + str(tabulkaStredZlomkova[pocetRiadkov][pozPivotaRiadok]))
        print(pozPivotaRiadok)
        print(poz)
        bazaTabulka[pozPivotaRiadok] = tabulkaStredNazvy[poz]
        print()
        tabulkaStredZlomkova = vydelPivotom(tabulkaStredZlomkova, pozPivotaRiadok, poz)
        tabulkaStredZlomkova = GCD(tabulkaStredZlomkova, pocetRiadkov, pocetStlpcov)
        tabulkaStredZlomkova = gaussEliminacnaMetoda(tabulkaStredZlomkova, pozPivotaRiadok, poz, pocetStlpcov)
        tabulkaStredZlomkova = GCD(tabulkaStredZlomkova, pocetRiadkov, pocetStlpcov)
        vypisDefaultSimplex(tabulkaStredZlomkova)
        print("//////////////////////////////// '♦' ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")


