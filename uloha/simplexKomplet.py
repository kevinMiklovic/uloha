#SIMPLEX kevin miklovic
#FUKNCIE PRE ZISTENIE
def hladanieZaporuVPomocnych(tabulka, pocetPomocnych, pocetStlpcov, pocetRiadkov):
    pocet = pocetStlpcov - pocetPomocnych
    akyRiadok = [0] * pocetRiadkov
    for i in range(0, pocetRiadkov):
        for j in range(pocet, pocetStlpcov):
            #print(tabulka[i][j], end=" ")
            if tabulka[i][j] != 0:
                akyRiadok[i] = 1
        #print("je to riadok: " + str(i))
        #print()
    #pretypovanePole = [eval(i) for i in akyRiadok]
    return akyRiadok #posielame naspat pole ktore obsahuje riadky pre vypocet 'W'
def vytvorenieW(tabulka, polePreVypocetW, wTabulka, pocetRiadkov, pocetStlpcov, pocetPomocnych, bTabulka):
    wVysledok = 0
    for i in range(0, pocetRiadkov):
        if polePreVypocetW[i] == 1:
            for j in range(0, pocetStlpcov-pocetPomocnych):
                wTabulka[j] = tabulka[i][j] + (wTabulka[j])
            wVysledok = wVysledok + bTabulka[i]
    wVysledok = wVysledok * (-1)
    for i in range(0, len(wTabulka)):
        wTabulka[i] = wTabulka[i] * (-1)

    return (wTabulka, wVysledok)
def findLowestNumberW(wTabulka, pocetStlpcov, pocetPomocnych):
    lowestNumber = 0
    poz = "nema zapornu hodnotu"
    for i in range(0, pocetStlpcov):
        if (lowestNumber > wTabulka[i]):
            lowestNumber = wTabulka[i]
            poz = i
    return poz, lowestNumber

def findPivot(tabulka, bTabulka, poziciaPivot, pocetRiadkov): #poziciaPivot - kde hladat pivota
    print(tabulka, bTabulka, poziciaPivot, pocetRiadkov)
    for i in range(0, pocetRiadkov):
        hodnota = 1337
        if (tabulka[i][poziciaPivot] > 0) and (bTabulka[i] > 0):
            print("♥♥♥")
            temp = bTabulka[i] / tabulka[i][poziciaPivot]
            print(bTabulka[i])
            print(tabulka[i][poziciaPivot])
            print(temp)
            print("♥♥♥")
            if (hodnota > temp):
                print("♣♣♣")
                hodnota = temp
                vyslednaPozPivota = i
                hodnotaPivota = tabulka[i][poziciaPivot]
                print("hodnotaPivota: " + str(hodnotaPivota))
                print("vyslednaPozPivota: " + str(vyslednaPozPivota))
                print("hodnotaPivota: " + str(hodnotaPivota))
    print("☻♥")
    print("hodnotaPivota: " + str(hodnotaPivota))
    print("vyslednaPozPivota: " + str(vyslednaPozPivota))
    print("hodnotaPivota: " + str(hodnotaPivota))




"""def findPivot(tabulka):
    najnizsiaHodnota = 0
    pozicia = 0
    for i in range(len(tabulkaStred[0])):
        print(zTabulka[0][i], end=" ")
        if (najnizsiaHodnota > zTabulka[0][i]):
            najnizsiaHodnota = zTabulka[0][i]
            pozicia = i
        print(str("najZapornejsia hodnota je: ") + str(najnizsiaHodnota) + str(" s poziciou: ") + str(pozicia) + str("\n"))
    return (najnizsiaHodnota, pozicia)
def findMyPivot(tabulka, pozicia, pocetRiadkov):
    for i in range(0, pocetRiadkov):"""


pocetPomocnych = 2
tabulkaStredNazvy = [["x1","x2","p1","p2","u1","u2"]]
tabulkaStred = [[3, 2, 0, 0, 1, 0],
                [2, -4, -1, 0, 0, 1],
                [4, 3, 0, 0, 0, 0]]

bTabulka = [14, 2, 19]
zTabulka = [3, 2, 0, 0, 0, 0]
zVysledok = 0
wTabulka = [0, 0, 0, 0, 0, 0]
wVysledok = 0


pocetRiadkov = len(tabulkaStred)
pocetStlpcov = len(tabulkaStred[0])
print("\n\npocet stlpcov v prvej tabulke je: " + str(pocetStlpcov) + " a pocet riadkov je: " + str(pocetRiadkov))
print("♦♦♦♦♦♦♦♦♦♦")

polePreVypocetW = hladanieZaporuVPomocnych(tabulkaStred, pocetPomocnych, pocetStlpcov, pocetRiadkov)
polePreVypocetW = (polePreVypocetW)
vysledneDveHodnoty = vytvorenieW(tabulkaStred, polePreVypocetW, wTabulka, pocetRiadkov, pocetStlpcov, pocetPomocnych, bTabulka)
wTabulka = vysledneDveHodnoty[0]        #vracaju sa z funkcie 2 hodnoty: [0] - pre pole'Z'
wVysledok = vysledneDveHodnoty[1]       #[1] - pre vysledne w
print(str("bázová hodnota pre 'W' je: ") + str(wVysledok) + str(" hodnoty v riadku 'W': ") + str(wTabulka))
#hladaniePivotaPoz[] - prva hodnota je pozicia a druha je hodnota
hladaniePivotaPoz = findLowestNumberW(wTabulka, pocetStlpcov, pocetPomocnych)

if (hladaniePivotaPoz[1] == 0):
    print("PROGRAM NEMA RIESENIE CEZ 'W'")
else:
    print("\n\n☺☺☺☺☺☺☺☺☺☺☺☺ MAME NEGATIVNE CISLO")
    print(hladaniePivotaPoz[0])
    findPivot(tabulkaStred, bTabulka, hladaniePivotaPoz[1], pocetRiadkov)




#prve cislo reprezentuje hodnotu a druhe poziciu
#lowersNumber = findLowestNumber(zTabulka)
