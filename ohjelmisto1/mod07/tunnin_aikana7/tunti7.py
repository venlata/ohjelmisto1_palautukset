#Tunti 7, Funktiot
def f(x):
    print(x)
    return 3
print(f(7))

#Tyhjä funktio:
#Sen saa palauttamaan None-valuen jos laittaa printin tuonne loppuun
def funk1():
    print("hee hee")
print(funk1())

#Useita argumentteja voi sijoittaa funktioon:
def funk2(m, y):
    print(m)
    print(y)
    print("Moi")
    print(2*m)
    # return 77
print(funk2(2, 6))
#Jos return ei ole, tulee myös perään None value

#
g = [1, 2, 3]
o = g.append(4)
print(o) #Tästä tulee vain None koska append on funktio
print(g) #Tästä tulee se oikea lopputulos koska g on lista

#2 lukua funktioon, palauta niiden summa:
def funk3(c, q):
    return c+q
print(funk3(2, 5)) #Tähän tulee ne arvot jotka syötetään funktion muuttujille

#Palauttaa Terve John!:
def funk4(v):
    return (f"Terve, {v}!")
print(funk4("John"))

#Funktio jolla on kolme argumenttia, n, h, ja nimi
#Jos nimi on "summa", funktio palauttaa n + h
#Jos nimi on "erotus", funktio palauttaa n - h
def funk5(n, h, nimi):
    if nimi == "summa":
        return n+h
    elif nimi == "erotus":
        return n-h
print(funk5(6, 2, "summa"))
print(funk5(6, 2, "erotus"))

#Funktio joka palauttaa siihen syötetyn listan parilliset luvut
def funk6(listamme):
    
    lista2 = []
    for numba in listamme:
        if numba % 2 == 0:
            lista2.append(numba)
    return lista2

lista1 = [1, 23, 4, 6, 9, 34, 2, 77]
print(funk6(lista1)) #koska lista1 on nyt funktion sisässä, "lista 1" == argumentti "listamme"

#Funktio "nimeni"
def nimeni(nimi, kerta):
    for kerrat in range(kerta):
        print(f"{nimi} {kerrat+1}. kerta")
    return ":)"
print(nimeni("Venla", 5))

#Lokaali vs. globaali
def funk7(i):
    i = i + 1
    print(i)

i = 19
funk7(i)
print(i)

#Lista muistetaan globaalisti:
def funk8(w):
    w.append(2)
    print(w)

w = [1, 3, 5]
funk8(w)
print(w)

