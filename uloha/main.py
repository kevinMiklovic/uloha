"""
def matica_nasobenie(matica1, matica2):
    for i in range(0,len(matica_1)):
        #riadok_vysledna_matica = []
        temp=[]                           #list pre output riadku
            for j in range(0,len(matica_2[0])):
                total=0
                l = 0
                for k in range(0,len(matica_1[0])):
                total += matica_1[i][k] * matica_2[l][j]
                l = l+1
            temp.append(total)
        vysledok.append(temp)
    return vysledok
"""



#######################################################
#######################################################
#######################################################
"""
print("MATICA 1")
r1 = (int(input("pocet riadkov matice ")))
s1 = (int(input("pocet stlpcov matice ")))
matica_1 = []
for i in range(r1):
   print("Napis cisla riadku: ",i+1, "pocet hodnot pre zadanie:", s1)
   riadok = list(map(int, input().split()))
   matica_1.append(riadok)
print("MATICA 2")
r2 = (int(input("pocet riadkov matice ")))
s2 = (int(input("pocet stlpcov matice ")))
matica_2 = []
for i in range(r2):
   print("Napis cisla riadku: ",i+1, "pocet hodnot pre zadanie:", s2)
   riadok = list(map(int, input().split()))
   matica_2.append(riadok)

matica_vysledok = []        #vysledna matica pre operacie
print("AKA OPERACIA MA NASTAT:\n 1-scitanie     2-odcitanie     3-nasobanie \n")
odpoved = int(input("Zadaj cislo"))
if(odpoved==1 and r1==r2 and s1==s2):
    for i in range(r1):
        for j in range(s1):
            matica_vysledok[i][j] = matica_1[i][j] + matica_2[i][j]
elif(odpoved == 2 and r1==r2 and s1==s2):
    for i in range(r1):
        riadok = []
        for j in range(s1):
            riadok.append(0)
            matica_vysledok.append(riadok)
            matica_vysledok[i][j] = matica_1[i][j] - matica_2[i][j]
elif (odpoved == 3 and s1 == r2):
    
        
for riadok in matica_1:
      print(riadok)
      print("  *  ")
for riadok in matica_2:
      print(riadok)
print()
print(matica_vysledok)
"""
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
##################                      MATICE                  #####################################################
#####################################################################################################################
print("\n-----MATICE-----\n")
print('MATICA A:')
a_riadok = int(input("Zadaj pocet riadkov matice: "))
a_stlpec = int(input("Zadaj pocet stĺpcov matice: "))
print('MATICA B:')
b_riadok = int(input("Zadaj pocet riadkov matice: "))
b_stlpec = int(input("Zadaj pocet stĺpcov matice: "))

#INICIALIZACIA MATICE A a B
matica_a = []
matica_b = []
matica_nasobanie = []

matica1 = []
matica2 = []
for i in range(a_riadok):
   print("Napis cisla riadku: ",i+1, "pocet hodnot pre zadanie:", a_riadok)
   riadok = list(map(int, input().split()))
   matica1.append(riadok)
for i in range(a_riadok):
   print("Napis cisla riadku: ",i+1, "pocet hodnot pre zadanie:", b_riadok)
   riadok = list(map(int, input().split()))
   matica2.append(riadok)
print("******************************************************")
print("Matica A: ", a_riadok, "x", a_stlpec)
for i in range(a_riadok):
    for j in  range(a_stlpec):
        print(matica1[i][j], end=" ")
    print()
print("Matica B: ", b_riadok, "x", b_stlpec)
for i in range(b_riadok):
    for j in  range(b_stlpec):
        print(matica2[i][j], end=" ")
    print()
print("******************************************************")
print("AKA OPERACIA MA NASTAT:\n 1-scitanie     2-odcitanie     3-nasobanie")
odpoved = int(input("Zadaj cislo: "))
if(odpoved==1 and a_riadok==b_riadok and a_stlpec==b_stlpec):
    for i in range(a_riadok):
        for j in range(a_stlpec):
            matica1[i][j] = matica1[i][j] + matica2[i][j]
elif (odpoved == 2 and a_riadok == b_riadok and a_stlpec == b_stlpec):
    for i in range(a_riadok):
        for j in range(a_stlpec):
            matica1[i][j] = matica1[i][j] - matica2[i][j]
elif (odpoved == 3 and a_stlpec == b_riadok):
    for i in range(a_riadok):
        for j in range(a_stlpec):
            for k in range(a_riadok):
                matica_nasobanie[i][j] = matica_nasobanie[i][j] + matica1[i][k] * matica2[k][j]
print("******************************************************")
print("VYSLEDOK:")
for i in range(b_riadok):
    for j in  range(b_stlpec):
        print(matica1[i][j], end=" ")
    print()


#####################################################################################################################
##################                      ZLOMKY                  #####################################################
#####################################################################################################################
print("\n-----ZLOMKY-----\n")
print("Zlomok 1")
citatel1 = int(input("Zadaj CITATELA zlomku: "))
menovatel1 = int(input("Zadaj MENOVATELA zlomku: "))
print("Zlomok 2")
citatel2 = int(input("Zadaj CITATELA zlomku: "))
menovatel2 = int(input("Zadaj MENOVATELA zlomku: "))
vysledokCitatel = 0
vysledokMenovatel = 0
print("******************************************************")
print("AKA OPERACIA MA NASTAT:\n 1-scitanie     2-odcitanie     3-nasobanie     4-delenie")
odpoved = int(input("Zadaj cislo: "))
if(odpoved == 1):
    if menovatel1 == menovatel2:
        vysledokCitatel = citatel1 + citatel2
        vysledokMenovatel = menovatel1
    else:
        vysledokMenovatel = menovatel1
        vysledokCitatel = citatel1
        menovatel1 = menovatel1 * menovatel2
        citatel1 = citatel1 * menovatel2
        menovatel2 = menovatel2 * vysledokMenovatel
        citatel2 = citatel2 * vysledokCitatel
        vysledokCitatel = citatel1 + citatel2
        vysledokMenovatel = menovatel1
elif(odpoved==2):
    if menovatel1 == menovatel2:
        vysledokCitatel = citatel1 - citatel2
        vysledokMenovatel = menovatel1
    else:
        vysledokMenovatel = menovatel1
        vysledokCitatel = citatel1
        menovatel1 = menovatel1 * menovatel2
        citatel1 = citatel1 * menovatel2
        menovatel2 = menovatel2 * vysledokMenovatel
        citatel2 = citatel2 * vysledokCitatel
        vysledokCitatel = citatel1 - citatel2
        vysledokMenovatel = menovatel1
elif(odpoved==3):
    vysledokCitatel = citatel1 * citatel2
    vysledokMenovatel = menovatel1 * menovatel2
elif(odpoved==4):
    vysledokCitatel = citatel1 * menovatel2
    vysledokMenovatel = menovatel1 * citatel2
print("VYLEDOK\n",vysledokCitatel,"\n---\n",vysledokMenovatel)
print()


#def createZlomok1():
#    citatel.int(input("Zadaj CITATELA zlomku: "))
#    menovatel.int(input("Zadaj MENOVATELA zlomku: "))
#    return
#def createZlomok2():
#    a
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
"""
for i in range(a_riadok):
    print("Napis riadok", i, "matice")
    riadok = list(int(input().split()))
    matica1.append(riadok)
print("Matica 1:", matica1)

#NACITANIE CISEL DO MATICE
for i in range(a_riadok):
    cislo = []
    for j in  range(a_stlpec):
        cislo.append(int(input("cislo pre poziciu: ")))
        matica_a.append(cislo)

#NACITANIE CISEL DO MATICE
for i in range(b_riadok):
    cislo = []
    for j in  range(b_stlpec):
        cislo.append(int(input("cislo pre poziciu: ")))
    matica_b.append(cislo)

print()
#VYPISANIE MATICE
for i in range(a_riadok):
    for j in  range(a_stlpec):
        print(matica_a[i][j], end=" ")
    print()

#VYPISANIE MATICE
for i in range(b_riadok):
    for j in  range(b_stlpec):
        print(matica_b[i][j], end=" ")
    print()

#OPERACIE MATIC
print("AKA OPERACIA MA NASTAT:\n 1-scitanie     2-odcitanie     3-nasobanie \n")
odpoved = int(input("Zadaj cislo"))
if(odpoved==1 and a_riadok==b_riadok and a_stlpec==b_stlpec):
    for i in range(b_riadok):
        for j in range(b_stlpec):
            matica_a[i][j] = matica_a[i][j] + matica_b[i][j]
    for i in range(a_riadok):
        for j in range(a_stlpec):
            print(matica_a[i][j], end=" ")
        print()
if (odpoved == 2 and a_riadok == b_riadok and a_stlpec == b_stlpec):
    for i in range(b_riadok):
        for j in range(b_stlpec):
            matica_a[i][j] = matica_a[i][j] - matica_b[i][j]
    for i in range(a_riadok):
        for j in range(a_stlpec):
            print(matica_a[i][j], end=" ")
        print()

if (odpoved == 3 and a_stlpec == b_riadok):
    for i in range(a_riadok):
        for j in range(a_stlpec):
            

            for k in range(b_stlpec):
                matica_nasobanie[i][j] += matica_a[i][k] * matica_b[k][j]
    for i in range(a_riadok):
        for j in range(b_stlpec):
            print(matica_nasobanie[i][j], end=" ")
        print()

print('\nSTALE ZIJEM')
"""