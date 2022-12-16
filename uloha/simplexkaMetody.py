import sys
def hladanieNulovehoriadkuW(wTabulka, pocetStlpcov, pocetPomocnychU):
    a = 1
    pocetStlpcov = pocetStlpcov - pocetPomocnychU
    for i in range(1, pocetStlpcov):
        if wTabulka[0][i][0] == 0:
            a = a + 1
    if a == pocetStlpcov:
        print("CELY VEKTOR JE NULOVY!!!!!!!!!!!!")
        return 'koniec'
    else:
        print("Cenova funkcia sa moze dalej optimalizovat - nie je NENULOVA")
def vytvorW(tabulkaDefault, wTabulka, pocet_U, pomocnePrePocetRiadkov):
    riadok = 0
    if pocet_U > 0:
        for i in range(len(tabulkaDefault)-1):
            for j in range(len(tabulkaDefault[0])):
                if (pomocnePrePocetRiadkov[0][riadok] > 0):
                    wTabulka[0][j][0] = wTabulka[0][j][0] + (tabulkaDefault[i][j][0] * (-1))
            riadok = riadok + 1
        return wTabulka
def zistiKolkoRiadkovPre_W(tabulka, pocet_P, pocet_U, pocet_Stlpcov, pocet_Riadkov):
    pomocna = pocet_Stlpcov - pocet_P - pocet_U
    odAkehoIdeme = pomocna + pocet_P
    akyRiadokSpocitat = [ [0] * (pocet_U + 1) ]
    pocet_Riadkov = pocet_Riadkov - 1
    for i in range(0, pocet_Riadkov):
        for j in range(odAkehoIdeme, pocet_Stlpcov):
            if (tabulka[i][j] == 1):
                akyRiadokSpocitat[0][i] = 1
    return akyRiadokSpocitat
def zistiNajvacsieZaporneCislo(wTabulka, poc_stlpcov, pocetU):
    najmensieCislo = 1000
    for i in range(1, poc_stlpcov):
        pomocna = wTabulka[0][i][0] / wTabulka[0][i][1]
        if pomocna < najmensieCislo:
            najmensieCislo = pomocna
            pozicia = i
    if pozicia >= 0:
        return pozicia
    else:
        print(wTabulka)
        print("NEDA SA DALEJ UPRAVIT - nemame zaporne hodnoty")
        return "NEDA SA DALEJ UPRAVIT - nemame zaporne hodnoty"
def gaussMetodForW(tabulka, wTabulka, pivotRiadok, pivotStlpec, pocetStlpcov):
    pocetStlpcov = pocetStlpcov - 1
    #print(wTabulka)
    #print(pocetStlpcov)
    #print(pivotRiadok)
    ulozPivotaCitatel = wTabulka[0][pivotStlpec][0]
    ulozPivotMenovatel = wTabulka[0][pivotStlpec][1]
    #print("hodnoty z wTabulky - pivot")
    #print(ulozPivotaCitatel)
    #print(ulozPivotMenovatel)

    for i in range(0, pocetStlpcov):
        if ulozPivotMenovatel == 0:
            print("JE TO AKO TOTALNE V PICIIIIIIIII TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
            return wTabulka
        else:
            """print("//////////// pocitame //////////////")
            print("hodnoty z tabulky a nasobenie pivotom - "+ str(tabulka[pivotRiadok][i][0]) +" * "+ str(ulozPivotaCitatel))
            print("hodnoty z tabulky a nasobenie pivotom - " + str(tabulka[pivotRiadok][i][1]) + " * " + str(ulozPivotaCitatel))"""

            tempCitatel = tabulka[pivotRiadok][i][0] * ulozPivotaCitatel
            tempMenoval = tabulka[pivotRiadok][i][1] * ulozPivotMenovatel
            if tempMenoval == wTabulka[0][i][1]:
                wTabulka[0][i][0] = wTabulka[0][i][0] - tempCitatel
            else:
                """print("vyledok? - " + str(tempCitatel) + " * " + str(wTabulka[0][i][1]))
                print("vyledok? - " + str(wTabulka[0][i][0]) + " * " + str(tempMenoval))
                print("vyledok? - " + str(wTabulka[0][i][1]) + " * " + str(tempMenoval))"""
                tempCitatel = tempCitatel * wTabulka[0][i][1]
                wTabulka[0][i][0] = wTabulka[0][i][0] * tempMenoval
                wTabulka[0][i][1] = wTabulka[0][i][1] * tempMenoval
                """print(tempCitatel)
                print(wTabulka[0][i][0])
                print(wTabulka[0][i][1])
                print("vyledok? - " + str(wTabulka[0][i][0]) + " - " + str(tempCitatel))"""
                wTabulka[0][i][0] = wTabulka[0][i][0] - tempCitatel
    return wTabulka
#################################################################
################## ↑↑↑ PRE 'W' SIMPLEXKU ↑↑↑ ##################
################## ↓↓↓ PRE KAZDU SIMPLEXKU ↓↓↓ ##################
#################################################################
def GCD(tabulka, pocetRiadkov, pocetStlpcov):
    for i in range(0, pocetRiadkov):
        for j in range(0, pocetStlpcov):
            pivotCitatel = tabulka[i][j][0]
            pivotMenovatel = tabulka[i][j][1]
            if tabulka[i][j][0] == 0:
                tabulka[i][j][0] = 0
                tabulka[i][j][1] = 1
            elif (pivotMenovatel >= pivotCitatel):
                pomocna = pivotCitatel
                if pomocna < 0:
                    pomocna = pomocna * (-1)
                elif pomocna == 0:
                    pomocna = 1
                while (pomocna != 1):
                    if ((pivotCitatel % pomocna) == 0) and ((pivotMenovatel % pomocna) == 0):
                        tabulka[i][j][0] = tabulka[i][j][0] / pomocna
                        tabulka[i][j][1] = tabulka[i][j][1] / pomocna
                        pomocna = 1
                    else:
                        pomocna = pomocna - 1
            else:
                pomocna = pivotMenovatel
                while (pomocna != 1):
                    if ((pivotCitatel % pomocna) == 0) and ((pivotMenovatel % pomocna) == 0):
                        tabulka[i][j][0] = tabulka[i][j][0] / pomocna
                        tabulka[i][j][1] = tabulka[i][j][1] / pomocna
                        pomocna = 1
                    else:
                        pomocna = pomocna - 1
    return tabulka
def vyberPivota(tabulka, pozZaporneho, pocetRiadkov):
    pocetRiadkov = pocetRiadkov - 1
    najmensieCislo = 10000
    for i in range(0, pocetRiadkov):
        if ((tabulka[i][0][0] >= 0) and (tabulka[i][pozZaporneho][0] > 0)):
            citatel = tabulka[i][0][0] * tabulka[i][pozZaporneho][1]
            menovatel = tabulka[i][0][1] * tabulka[i][pozZaporneho][0]
            vysledokDocasne = citatel / menovatel
            print("♠Delenie bazovej hodnoty s vektorovou:     BAZA " + str(i) + " - " + str(tabulka[i][0]) + " / " + str(
                tabulka[i][pozZaporneho]) + " a jeho vysledok je: " + str(vysledokDocasne))
            if najmensieCislo > vysledokDocasne:
                najmensieCislo = vysledokDocasne
                pozPivota = i
        else:
            print("♦♦♦♦♦♦♦  Bohuzial sa neda vydelit BAZA " + str(i) + " - " + str(str(tabulka[i][0])) + str(tabulka[i][pozZaporneho]))
    if najmensieCislo >= 0:
        return pozPivota
    elif najmensieCislo == 10000:
        return 'totalnyKoniec'
def vydelPivotom(tabulka, riadokPivota, stlpecPivota):
    #print("♥")
    #print(riadokPivota)
    #print(stlpecPivota)
    pivotCitatel = tabulka[riadokPivota][stlpecPivota][0]
    pivotMenovatel = tabulka[riadokPivota][stlpecPivota][1]
    #print(pivotCitatel)
    #print(pivotMenovatel)
    for j in range(len(tabulka[riadokPivota])):
        tabulka[riadokPivota][j][0] = tabulka[riadokPivota][j][0] * pivotMenovatel
        tabulka[riadokPivota][j][1] = tabulka[riadokPivota][j][1] * pivotCitatel
    return tabulka
def gaussEliminacnaMetoda(tabulka, pivotRiadok, pivotStlpec, pocetStlpcov):
    for i in range(len(tabulka)):
        tempPivotCitatel = tabulka[i][pivotStlpec][0]
        tempPivotMenovat = tabulka[i][pivotStlpec][1]
        """print(tempPivotMenovat)
        print(tempPivotMenovat)
        print("HALOOOO?")"""
        if pivotRiadok != i:
            if tabulka[i][pivotStlpec][0] != 0:
                for j in range(0, pocetStlpcov):
                    """print("###########################################################")
                    print(tempPivotCitatel)
                    print(tempPivotMenovat)
                    print("SME V CYKLE")"""
                    tempPivotRiadokCitatel = tabulka[pivotRiadok][j][0] * tempPivotCitatel
                    tempPivotRiadokMenovatel = tabulka[pivotRiadok][j][1] * tempPivotMenovat
                    """print(str(tabulka[pivotRiadok][j][0]) + " * " + str(tempPivotCitatel))
                    print(str(tabulka[pivotRiadok][j][1]) + " * " + str(tempPivotMenovat))
                    print("---")
                    print(tempPivotRiadokCitatel)
                    print(tempPivotRiadokMenovatel)
                    print("//////////")
                    print(tabulka[i][j][0])
                    print(tabulka[i][j][1])"""
                    #PRVY je menovatel riadku kde chceme mat 0 nad alebo pod pivotom - DRUHY je pivotov riadok
                    if tabulka[i][j][1] == tempPivotRiadokMenovatel:
                        tabulka[i][j][0] = tabulka[i][j][0] - tempPivotRiadokCitatel
                        #print("vyledok je: " + str(tabulka[i][j]))
                    else:
                        ulozMenovatelaPivotRiadok = tempPivotRiadokMenovatel
                        #print(str(tempPivotRiadokCitatel) +" * " +str(tabulka[i][j][1]))
                        #print(str(tempPivotRiadokMenovatel) + " * " + str(tabulka[i][j][1]))
                        tempPivotRiadokCitatel = tempPivotRiadokCitatel * tabulka[i][j][1]
                        tempPivotRiadokMenovatel = tempPivotRiadokMenovatel * tabulka[i][j][1]
                        #print(str(tabulka[i][j][0]) + " * " + str(ulozMenovatelaPivotRiadok))
                        #print(str(tabulka[i][j][1]) + " * " + str(ulozMenovatelaPivotRiadok))
                        tabulka[i][j][0] = tabulka[i][j][0] * ulozMenovatelaPivotRiadok
                        tabulka[i][j][1] = tabulka[i][j][1] * ulozMenovatelaPivotRiadok
                        #print(str(tabulka[i][j][1]) + " - " + str(tempPivotRiadokCitatel))
                        tabulka[i][j][0] = tabulka[i][j][0] - tempPivotRiadokCitatel
                        #print("vyledok je: " + str(tabulka[i][j]))
                        #print("**********")
                    #print("########################################################################")
    return tabulka
def vypisSimplexky(tabulka, wTabulka):
    print("\n ▬▬ VYPIS SIMPLEXKY ▬▬")
    pocetRiadkov = (len(tabulka)) - 1
    for i in range(len(tabulka)):
        if i == pocetRiadkov:
            print("-----")
            print("Z = "+str(tabulka[i]))
        else:
            print("b = "+str(tabulka[i]))
    print("W = "+str(wTabulka))
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")
def prehodTabulky(tabulka, pocetStlpcov, pocetU):
    pocetStlpcov = pocetStlpcov - (pocetU)
    pocetRiadkov = len(tabulka)
    #vytvorime pole velkosti minulej len s odrezanymi 'U' pomocnymi
    for i in range(0, pocetRiadkov):
        del tabulka[i][pocetStlpcov:]
        #print(tabulka[i])
        #print("koniec riadku")
    return tabulka
def zistenieZapornejSumy(tabulka):
    pocetRiadkov = len(tabulka) - 1
    najmensieCislo = 1000
    for i in range(1, len(tabulka[0])):
        pomocna = tabulka[pocetRiadkov][i][0] / tabulka[pocetRiadkov][i][1]
        if pomocna < najmensieCislo:
            najmensieCislo = pomocna
            pozicia = i
    if pozicia >= 0:
        return pozicia
    else:
        print("☺☺☺☺☺☺")
        print("NEDA SA DALEJ UPRAVIT!")
def hladajPivota(tabulka, poz):
    print()
    pomocna = 1000
    pocRiad = len(tabulka)
    for i in range(len(tabulka)-1):
        #print("PODMIENKA: " + str(tabulka[i][poz][0]) + " and " + str(tabulka[i][0][0]))
        if tabulka[i][poz][0] > 0 and tabulka[i][0][0] >= 0:
            """print("PODMIENKA SPLNENA")
            print("------: " + str(tabulka[i][0][0]) + " and " + str(tabulka[i][poz][1]))
            print("------: " + str(tabulka[i][0][1]) + " and " + str(tabulka[i][poz][0]))"""
            pomocnaCit = tabulka[i][0][0] * tabulka[i][poz][0]
            pomocnaDel = tabulka[i][0][1] * tabulka[i][poz][1]
            vysledok = pomocnaCit / pomocnaDel
            #print(vysledok)
            print(
                "♠Delenie bazovej hodnoty s vektorovou:     BAZA " + str(i) + " - " + str(tabulka[i][0]) + " / " + str(
                    tabulka[i][poz]) + " a jeho vysledok je: " + str(vysledok))
            if pomocna > vysledok:
                pozRiadok = i
        else:
            print("♦♦♦♦♦♦♦  Bohuzial sa neda vydelit BAZA " + str(i) + " - " + str(str(tabulka[i][0])) + str(tabulka[i][poz]))
    print()
    return pozRiadok
def vypisDefaultSimplex(tabulka):
    print("\n▬▬ VYPIS SIMPLEXKY ▬▬")
    a = len(tabulka)
    for i in range(len(tabulka)):
        if i == (a-1):
            print("-----")
            print("Z = " + str(tabulka[i]))
        else:
            print("b = " + str(tabulka[i]))
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")
def ukoncenie(tabulka, pocetStlpcov, pocetRiadkov):
    #print("ukonceie")
    pocetRiadkov = pocetRiadkov - 1
    pocet = tabulka[pocetRiadkov]
    #print("POCET RIADKOV")
    #print(pocetRiadkov)
    vysledok = 0
    print()
    for i in range(1, pocetStlpcov):
        if tabulka[pocetRiadkov][i][0] >= 0:
            #print(i)
            vysledok = vysledok + 1
            """print(tabulka[i][i][0])
            print("mame kladne cislo")
            print(vysledok)
            print()"""
    #print("podmienka: " +str(vysledok) + " == " + str(pocetStlpcov - 1))
    if vysledok == (pocetStlpcov - 1):
        print("SIMPLEXOVA METODA JE FINALNA")
        print(tabulka[pocetRiadkov])
        return '0'
    else:
        print("SIMPLEXOVA METODA NIE JE FINALNA")
        print(tabulka[pocetRiadkov])
        return '1'
