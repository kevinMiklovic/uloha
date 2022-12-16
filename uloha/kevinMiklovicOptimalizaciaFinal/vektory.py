######********************************************************************
def vytvorenieVektora(b):

    while True:
        b = input("Napis pocet hodnot pre " + str(b) + ": ")
        if b.isdigit():
            b = int(b)
            break
        else:
            print("Zadaj cislo a nie pismena alebo znaky!!!")

    a = [0]*b
    for i in range(0, b):
        a[i] = int(input("napis prvu hodnotu na pozici v intervale " + str(i+1) + " "))

    return a

######********************************************************************
def vypisVektora(vVysledok, v1, v2, a):

    print(str(a) + str(v1) + "\n" + str(v2) + "\nVYSLEDNY VEKTOR\n" + str(vVysledok))
    #for i in range(0, len(vektor)):
    #    print(str(a) + "prva hodnota v intervale: " + str(vektor[i]))

######********************************************************************
def sucetVektora(vektor1, vektor2):

    vysledok = [0]*len(vektor1)
    for i in range(0, len(vektor1)):
        vysledok[i] = vektor1[i] + vektor2[i]

    return vysledok

######********************************************************************
def odcitanieVektora(vektor1, vektor2):

    vysledok = [0] * len(vektor1)
    for i in range(0, len(vektor1)):
        vysledok[i] = vektor1[i] - vektor2[i]

    return vysledok

######********************************************************************
def nasobenieVektora(vektor1, vektor2):

    vysledok = [0] * len(vektor1)
    for i in range(0, len(vektor1)):
        vysledok[i] = vektor1[i] * vektor2[i]

    return vysledok