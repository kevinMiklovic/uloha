######********************************************************************
def vytvorMatica():

    while True:
        riadky = input("Napis pocet riadkov matice: ")
        if riadky.isdigit():
            riadky = int(riadky)
            break
        else:
            print("Zadaj cislo a nie pismena alebo znaky!!!")

    while True:
        stlpce = input("Napis pocet stlpcov matice: ")
        if stlpce.isdigit():
            stlpce = int(stlpce)
            break
        else:
            print("Zadaj cislo a nie pismena alebo znaky!!!")

    #print(type(riadky), type(stlpce))
    matica = []
    for i in range(riadky):
        pomocnaPreRiadok = []
        for j in range(stlpce):
            pomocnaPreRiadok.append(int(input("Zadaj hodnoty " + str(i+1) + " riadku a " + str(j+1) + " stlpca: ")))
        matica.append(pomocnaPreRiadok)

    return matica

######********************************************************************
def vypisMatice(mojaMatica, a):

    print("######### --- TOVJA MATICA " + a)
    for row in mojaMatica:
        for hodnota in row:
            print(hodnota, end=" ")
        print()

######********************************************************************
def sucinMatice(m1, m2):

    vyslednaMatica = []
    for i in range(0, len(m1)): #loop cez kazdy riadok prvej matice
        pomocna = [] #pomocna aby drzalo list s hodnotami
        for j in range(0, len(m2[0])): #loop cez stlpce druhej matice
            total = 0
            l = 0
            for k in range(0, len(m1[0])):
                total += m1[i][k]*m2[l][j]
                l = l+1
            pomocna.append(total)
        vyslednaMatica.append(pomocna)

    return vyslednaMatica

######********************************************************************
def scitanieMatice(m1, m2):

    vyslednaMatica = [ [0]*len(m1) for i in range(len(m2[0]))]
    for riadok in range(len(m1)):
        for stlpec in range(len(m2[0])):
            vyslednaMatica[riadok][stlpec] = m1[riadok][stlpec] + m2[riadok][stlpec]

    return vyslednaMatica

######********************************************************************
def odcitanieMatice(m1, m2):

    vyslednaMatica = [ [0]*len(m1) for i in range(len(m2[0]))]
    for riadok in range(len(m1)):
        for stlpec in range(len(m2[0])):
            vyslednaMatica[riadok][stlpec] = m1[riadok][stlpec] - m2[riadok][stlpec]

    return vyslednaMatica

######********************************************************************
def zistiVelkostMatice(matica):
    riadok = len(matica)
    stlpec = len(matica[0])
    return riadok, stlpec
