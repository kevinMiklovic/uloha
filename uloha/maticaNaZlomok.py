#uprava prvotnej matice na zlomkovu
def spravZlomkovu(tabulka):
    for i in range(len(tabulka)):
        for j in range(len(tabulka[0])):
            pomocna = spravZlomok(tabulka[i][j])
            tabulka[i][j] = pomocna
    return tabulka

#uprava cisla na zlomok
def spravZlomok(cislo):
    if (cislo == 0):
        vratZlomok = [cislo, 1]
    elif (cislo < 0):
        #cisloPomocne = cislo * (-1)
        vratZlomok = [cislo, 1]
    else:
        vratZlomok = [cislo, 1]
    return vratZlomok