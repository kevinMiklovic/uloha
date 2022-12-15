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
def zistiNajvacsieZaporneCislo(wTabulka, poc_stlpcov):
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
            print("hodnoty z tabulky a nasobenie pivotom - " + str(tabulka[pivotRiadok][i][1]) + " * " + str(ulozPivotaCitatel))
            """
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
    najmensieCislo = 1000
    for i in range(0, pocetRiadkov):
        print("Delenie bazovej hodnoty s vektorovou: " + str(tabulka[i][0]) + " / " +str(tabulka[i][pozZaporneho]) + " a jeho vysledok je: ")
        if ((tabulka[i][0][0] >= 0) and (tabulka[i][pozZaporneho][0] > 0)):
            citatel = tabulka[i][0][0] * tabulka[i][pozZaporneho][1]
            menovatel = tabulka[i][0][1] * tabulka[i][pozZaporneho][0]
            vysledokDocasne = citatel / menovatel
            print("VYSLEDOK JE: " + str(vysledokDocasne) + "\n")
            if najmensieCislo > vysledokDocasne:
                najmensieCislo = vysledokDocasne
                pozPivota = i
        else:
            print("☺☺☺☺☺☺☺☺☺☺☺☺Tak to mi ho vyndej ---- NEEXISTUJE MOZNY VYBER PIVOTA")
    if najmensieCislo >= 0:
        return pozPivota
def vydelPivotom(tabulka, riadokPivota, stlpecPivota):
    pivotCitatel = tabulka[riadokPivota][stlpecPivota][0]
    pivotMenovatel = tabulka[riadokPivota][stlpecPivota][1]
    for j in range(len(tabulka[riadokPivota])):
        tabulka[riadokPivota][j][0] = tabulka[riadokPivota][j][0] * pivotMenovatel
        tabulka[riadokPivota][j][1] = tabulka[riadokPivota][j][1] * pivotCitatel
    return tabulka
def gaussEliminacnaMetoda(tabulka, pivotRiadok, pivotStlpec, pocetStlpcov):
    for i in range(len(tabulka)):
        tempPivotCitatel = tabulka[i][pivotStlpec][0]
        tempPivotMenovat = tabulka[i][pivotStlpec][1]
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
                    print("NADOMNOU JE CHYBA")
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
"""
def gaussMetoda(tabulka, pivotRiadok, pivotStlpec, pocetStlpcov):
    print(tabulka[0])
    print(tabulka[1])
    print(tabulka[2])
    print(tabulka[3])
    for i in range(len(tabulka)):
        pomocnaPivotCitatel = tabulka[i][pivotStlpec][0]
        pomocnaPivotMenovatel = tabulka[i][pivotStlpec][1]
        if (i != pivotRiadok):
            if (tabulka[i][pivotStlpec][0] != 0):
                for j in range(0, pocetStlpcov):
                    citatelPivot = tabulka[pivotRiadok][j][0] * tabulka[i][pivotStlpec][0]
                    menovatelPivot = tabulka[pivotRiadok][j][1] * tabulka[i][pivotStlpec][1]
                    if tabulka[i][j][1] == menovatelPivot:
                        print("▼▼▼▼▼▼▼▼▼")
                        print("PRVA PODMIENKA")
                        #print(tabulka[i][j][0])
                        #print(tabulka[i][j][1])
                        print("▼▼▼▼▼▼▼▼▼\n")
                        tabulka[i][j][0] = tabulka[i][j][0] - citatelPivot
                        tabulka[i][j][1] = menovatelPivot
                    else:
                        print("☺ vypisujem riadok pre NULU:")
                        print(tabulka[i][j][0])
                        print(tabulka[i][j][1])
                        print(" vypisujem co riadok pivota: ")
                        print(tabulka[pivotRiadok][j][0])
                        print(tabulka[pivotRiadok][j][1])
                        print(" vypisujem nasobenie cisiel: ")
                        print(str(tabulka[pivotRiadok][j][0]) +" * "+ str(pomocnaPivotCitatel))
                        print(str(tabulka[pivotRiadok][j][1]) + " * " + str(pomocnaPivotMenovatel))
                        tempCitatel = tabulka[pivotRiadok][j][0] * pomocnaPivotCitatel
                        tempMenovatel = tabulka[pivotRiadok][j][1] * pomocnaPivotMenovatel
                        print("☺ vypisujem vysledok horneho nasobenia:")
                        print(tempCitatel)
                        print(tempMenovatel)
                        if tabulka[i][j][1] == tempMenovatel:
                            print("menovatel sedel *******************************")
                            tabulka[i][j][0] = tabulka[i][j][0] - tempCitatel
                        else:
                            docasnaMenovatelPrePivota = tabulka[i][j][1]
                            print(docasnaMenovatelPrePivota)
                            print("menovatel neseeeeeeeeeeeeedel *******************************")
                            print(str(tabulka[i][j][0]) + " * " + str(tempMenovatel))
                            print(str(tabulka[i][j][1]) + " * " + str(tempMenovatel))
                            tabulka[i][j][0] = tabulka[i][j][0] * tempMenovatel
                            tabulka[i][j][1] = tabulka[i][j][1] * tempMenovatel

                            print(str(tempCitatel) + " * " + str(docasnaMenovatelPrePivota))
                            print(str(tempMenovatel) + " * " + str(docasnaMenovatelPrePivota))
                            tempCitatel = tempCitatel * docasnaMenovatelPrePivota
                            tempMenovatel = tempMenovatel * docasnaMenovatelPrePivota
                            tabulka[i][j][0] = tabulka[i][j][0] - tempCitatel
                            tabulka[i][j][1] = tempMenovatel
                print("\n")
                print("\n")
                print("\n")
                print("CHODTE DO PHICEEEEEEEEEE")
    return tabulka
"""
def vypisSimplexky(tabulka, wTabulka):
    print("\n ▬▬ VYPIS SIMPLEXKY ▬▬")
    pocetRiadkov = len(tabulka) - 1
    for i in range(len(tabulka)):
        if i == pocetRiadkov:
            print("-----")
            print("Z = "+str(tabulka[i]))
        else:
            print("b = "+str(tabulka[i]))
    print("W = "+str(wTabulka))
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")

