def simlexM():
    tabulkaVrch = [[1, -7, -4, 0, 0, 0, 0]]

    tabulkaStred = [[0, 2, 1, 1, 0, 0, 20],
                    [0, 1, 1, 0, 1, 0, 18],
                    [0, 1, 0, 0, 0, 1, 8]]

    tabulkaNezname = [["z", "x1", "x2", "S1", "S2", "S3"]]

    tabulkaVlavo = [["S1"],
                    ["S2"],
                    ["S3"]]

    pocetRiadkov = len(tabulkaStred) - 1
    pocetStlpcov = len(tabulkaStred[0]) - 1
    print("pocet stlpcov v prvej tabulke je: " + str(pocetStlpcov) + " a pocet riadkov je: " + str(pocetRiadkov))
    print("♦♦♦♦♦♦♦♦♦♦")

    koniec = 0
    while koniec < 3:

        min = 0
        for i in range(len(tabulkaVrch[0])-1):
            print("TabVrch[0][i] je: " + str(tabulkaVrch[0][i]))
            hodnota = tabulkaVrch[0][i]
            if hodnota < 0 and hodnota < min:
                min = hodnota
                pozStlpec = i


        print("min je: " + str(min))
        print("posledna hodnota je: " + str(hodnota))
        print("pozStlpec je: " + str(pozStlpec))
        print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")

        a = True
        for i in range(0, pocetRiadkov+1):
            print("♥")
            print(tabulkaStred[i][pocetStlpcov])
            print(tabulkaStred[i][pozStlpec])
            print("♥")
            if tabulkaStred[i][pozStlpec] > 0 and tabulkaStred[i][pocetStlpcov] >= 0:
                if a == True:
                    min2 = tabulkaStred[i][pocetStlpcov] / tabulkaStred[i][pozStlpec]
                    pozRiadok = i
                    pivotHodnota = tabulkaStred[i][pozStlpec]
                    a = False
                    print("hodnota min2 je: " + str(min2) + " a hodnota pivotu je: " + str(pivotHodnota))
                print("○○○○○○○○○○○○○○○")
                min = tabulkaStred[i][pocetStlpcov] / tabulkaStred[i][pozStlpec]
                print(min)
                if min2 > min:
                    min2 = min
                    pozRiadok = i
                    pivotHodnota = tabulkaStred[i][pozStlpec]
                    print("hodnota min2 je: " + str(min2) + " a hodnota pivotu je: " + str(pivotHodnota))
                print("○○○○○○○○○○○○○○○")
            else:
                print("○○○○○○○○○○○○○○○ Neda sa delit..")


        print("\nnajmensia hodnota je: " + str(min2) + " a jej pozicia je - Stlpec: " + str(pozStlpec) + " Riadok: " + str(pozRiadok) + " | a hodnota pivota je: " + str(pivotHodnota))
        print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
        tabulkaStred = pivotUpravaRiadka(tabulkaStred, pozRiadok, pozStlpec, pivotHodnota)
        print(tabulkaStred)
        tabulkaStred = gaussovaPodlaPivota(tabulkaStred, pozRiadok, pozStlpec, pivotHodnota, pocetRiadkov, pocetStlpcov, tabulkaVrch)
        print(tabulkaStred)
        tabulkaVrch = gaussUpravaVrch(tabulkaStred, pozRiadok, pozStlpec, pivotHodnota, pocetRiadkov, pocetStlpcov, tabulkaVrch)
        print(tabulkaVrch)
        print("♣♦•◘○○6♥☻☺1♣♦♂☻☻♥▬▬▬▬▬▬▬▬")
        print("♣♦•◘○○6♥☻☺1♣♦♂☻☻♥▬▬▬▬▬▬▬▬")
        print("PRVE KOLO PREBEHLO!")
        print("♣♦•◘○○6♥☻☺1♣♦♂☻☻♥▬▬▬▬▬▬▬▬")
        print("♣♦•◘○○6♥☻☺1♣♦♂☻☻♥▬▬▬▬▬▬▬▬")
        koniec = koniec + 1
        #koniec = mamPokracovat(tabulkaVrch)

def pivotUpravaRiadka(tabStred, riadok, stlpec, pivotHodnota):

    for i in range(0, len(tabStred[riadok])):
        tabStred[riadok][i] = tabStred[riadok][i] / pivotHodnota
        print(tabStred[riadok][i])

    return tabStred

def gaussovaPodlaPivota(tabStred, riadok, stlpec, pivotHodnota, pocetRiadkov, pocetStlpcov, tabVrch):

    print(riadok, stlpec, pocetRiadkov, pocetStlpcov)
    """for i in (0, pocetRiadkov):
        print("♂♂☺♂♂")
        gausUpravaPrvku = tabStred[i][stlpec]
        print(gausUpravaPrvku)
        print("♂♂☺♂♂")
        for j in range(0, len(tabStred[i])):
            if i != riadok and gausUpravaPrvku != 0:
                tabStred[i][j] = tabStred[i][j] / gausUpravaPrvku
                #print(tabStred[i][j])
                #print("♥")
                #print(tabStred[i][stlpec])
                #print()
    print(tabStred)"""

    for i in range(0, pocetRiadkov):
        pivot2 = tabStred[i][stlpec]
        for j in range(0, len(tabStred[i])):
            print("SOM PRED CYKLOM!!!")
            if i != riadok and pivot2 != 0:
                print("SOM V CYKLE")
                print("hodnota na upravenie [i][j] " + str(tabStred[i][j]))
                print("hodnota ktorou upravujem -pivot2 " + str(pivot2))
                temp = tabStred[riadok][j]
                print("temp " + str(temp))
                temp = temp * pivot2
                temp = temp * -1
                print(str(temp) + " temp = [riadok][j] " + str(tabStred[riadok][j]) + " | pivot2 " + str(pivot2))
                tabStred[i][j] = tabStred[i][j] + temp
                print(tabStred[i][j])
                print()
            elif i != riadok and pivot2 == 0:
                temp = tabStred[riadok][j] * -1
                tabStred[i][j] = tabStred[i][j] + temp
            print(tabStred[i])


    """for i in range(0, pocetRiadkov):
        print("☺☺☺")
        print()
        print(gausUpravaPrvku)
        print()
        print("☺☺☺")
        #print("pocet riadkov " + str(pocetRiadkov) + " i: " + str(i) + " riadok: " + str(riadok))
        for j in range(0, len(tabStred[i])):
            if i != riadok:
                #print(tabStred[i][j])
                #print(tabStred[riadok][j])
                temp = tabStred[riadok][j] * gausUpravaPrvku
                vysledna = tabStred[i][j] + temp
                tabStred[i][j] = vysledna

                #vysledna = tabStred[i][j] - tabStred[riadok][j]        #pre delenie a ocitanie
                #print("vysledok po odcitani: " +str(vysledna))
                #tabStred[i][j] = vysledna
                #print("vysledok v poli: " + str(tabStred[i][j]))
                #print("♂♂♂")
        #print("presiel som riadok")
        #print(tabStred[i])
        #print("♥")
    #print(tabStred)"""

    return tabStred

def gaussUpravaVrch(tabStred, riadok, stlpec, pivotHodnota, pocetRiadkov, pocetStlpcov, tabVrch):
    gausUpravaPrvku = tabVrch[0][stlpec]
    gausUpravaPrvku = gausUpravaPrvku * -1

    for i in range(len(tabVrch[0])):
        temp = tabStred[riadok][i] * gausUpravaPrvku
        vysledna = tabVrch[0][i] + temp
        tabVrch[0][i] = vysledna
    return tabVrch

def mamPokracovat(tabVrch):
    a=0
    for i in range(0, len(tabVrch[0])):
        if tabVrch[0][i] < 0:
            a = a + 1
    if a > 0:
        return 1
    else:
        return 0









#♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠
#♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠
#♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠
#♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠
#♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠
#♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠
#♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠
#♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠
#♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠ ♥♦♣♠
################################################################################
####☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺#
################################################################################
def easySimplexMethod():

    tabulkaNezname = [ "x1", "x2", "x3", "d1", "d2", "d3"]

    tabulkaStred = [ [1, 0, 0,    1, 0, 0],
                     [1, 1, 2,    0, 1, 0],
                     [0, 3, 4,    0, 0, 1] ]

    riadkyStred = len(tabulkaStred)
    stlpceStred = len(tabulkaStred[0])
    print(riadkyStred, stlpceStred)

    tabulkaBaza = [["-"] * riadkyStred]
    print(tabulkaBaza)

    jednotkovyVektorPole = [[0] * riadkyStred]
    print(jednotkovyVektorPole)
    nasiel = 0
    poziciaBaza = 0
    poziciaVrch = 0
    print("---------------------------------------")

    for i in range(len(tabulkaStred[0])):
        jednotkovyVektor=0
        b = 0
        for j in tabulkaStred:
            jednotkovyVektor+=j[i]
            print(j[i], end="♥ ")
            jednotkovyVektorPole[0][b] = j[i]
            b+=1
            if j[i] == 1:
                poziciaVrch = b
            poziciaBaza = i
            print()
        print()
        if jednotkovyVektor == 1:
            print("☻☻☻☻☻")
            nasiel = nasiel+1
            print("pozicia pre bazu - " + str(poziciaBaza+1))
            print(jednotkovyVektorPole)
            print("pozicia pre vrch - " + str(poziciaVrch) + "\n")
            tabulkaBaza[0][poziciaVrch] = tabulkaNezname[0][poziciaBaza]

    print(tabulkaBaza)



    tabulka = [ ["-",     "-",      1,   2,   4,       0,   0,     0,            "-",               "-"   ],
                ["Ci",  "BÁZA",    "x1", "x2", "x3",  "d1", "d2", "d3",    "PRAVA STRANA",      "PODIELY" ],
                [ 0,     "-",       1,   0,    0,      1,   0,     0,             2,                "-"   ],
                [ 0,     "-",       1,   1,    2,      0,   1,     0,             4,                "-"   ],
                [ 0,     "-",       0,   3,    4,      0,   0,     1,             6,                "-"   ],
                ["-",    "-",       0,   0,    0,      0,   0,     0,           "ZISK",             "▬"  ] ]

    
    ### 1. krok - zapis bázy - hladame jednotkove vektory
    jednotkovyVektor = 0

    riadky = len(tabulka)
    stlpce = len(tabulka[0])
    print(riadky, stlpce)

    sucet = 0
    pomPreBazu = [ [0]*(riadky-3)]
    print(pomPreBazu)
    print("☼☼☼☼☼☼☼☼☼☼☼")
    ABC = 2
    for i in range(2, stlpce-2):
        for j in tabulka:
            #print(j[i])
            pomPreBazu[j] = j[i]
        print(pomPreBazu)
        print("♂♂♂♂")
        #if i == stlpce-3:
        #    break

    print("☼☼☼☼☼☼☼☼☼☼☼")


    print("♦♦♦♦♦♦♦")
    for i in range(2, len(tabulka) - 1):  # vyberie "stred" - odstrihne
        pomocna = []
        pomocna.append("▬")
        for j in range(0, len(tabulka[0])):
            #pomocnaPreStlpec = 0
            pomocna.append(tabulka[i][j])
        pomocna.append("▬")
    print(pomocna)
    print("♦♦♦♦♦♦♦")

    print("♀♀♀♀♀♀♀♀♀♀")
    for i in range(2, len(tabulka)-1): #vyberie "stred" - odstrihne
        for j in range(2, len(tabulka[0])):
            print(tabulka[i][j])
        break
    print("♀♀♀♀♀♀♀♀♀♀")

    for i in range(2, len(tabulka)-1):
        for j in range(2, len(tabulka[0])):
            if tabulka[j] >= 1:
                jednotkovyVektor = jednotkovyVektor + 1
                pozicia = j

    #vypisSimplexTabulky(tabulka)


######********************************************************************
def vypisSimplexTabulky(tabulka):

    print("######### --- TOVJA VYSLEDNA TABUKJA")
    for row in tabulka:
        for hodnota in row:
            print(hodnota, end=" ")
        print()