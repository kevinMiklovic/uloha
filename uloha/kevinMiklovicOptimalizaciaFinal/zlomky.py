######********************************************************************
def vytvorZlomok():

    while True:
        a = input("Napis citatela: ")
        b = input("Napis menovatela: ")
        if a.isdigit() and b.isdigit():
            a = int(a)
            b = int(b)
            break
        else:
            print("Zadaj cislo a nie pismena alebo znaky!!!")

    return a, b

######********************************************************************
def vypisZlomku(zlomok):
    print("☻☻☻☻☻☻ Tvoj zlomok po scitani je:\n" + str(zlomok[0]) + "\n----\n" + str(zlomok[1]))

######********************************************************************
def sucetZlomkov(z1, z2):
    
    vysledok = [0, 0]
    if z1[1] == z2[1]:
        vysledok[0] = z1[0] + z2[0]
        vysledok[1] = z1[1]
    else:
        vysledok[1] = z1[1] * z2[1]
        vysledok[0] = (z1[0] * z2[1]) + (z2[0] * z1[1])

    return vysledok

######********************************************************************
def odcitanieZlomkov(z1, z2):

    vysledok = [0, 0]
    if z1[1] == z2[1]:
        vysledok[0] = z1[0] - z2[0]
        vysledok[1] = z1[1]
    else:
        vysledok[1] = z1[1] * z2[1]
        vysledok[0] = (z1[0] * z2[1]) - (z2[0] * z1[1])

    return vysledok

######********************************************************************
def nasobenieZlomkov(z1, z2):

    vysledok = [0, 0]
    vysledok[0] = z1[0] * z2[0]
    vysledok[1] = z1[1] * z2[1]

    return vysledok

######********************************************************************
def delenieZlomkov(z1, z2):

    vysledok = [0, 0]
    vysledok[0] = z1[0] * z2[1]
    vysledok[1] = z1[1] * z2[0]

    return vysledok