#Tehtävä 7 osa 1
import random
import math
# def paluun():
#     return random.randint(1,6)
# paluun()
# numba = paluun()
# #Pääohjelma
# while numba != 6:
#     print(numba)
#     numba = paluun()
# print(numba)

#Tehtävä 7 osa 2
def paluun(kaikkitahkot):
    return random.randint(1, kaikkitahkot)
valinta = int(input("Anna nopan tahkot: "))
while True:
    maara = paluun(valinta)
    print(maara)
    if maara == valinta:
        break

#Tehtävä 7 osa 3

def muunnos(gallona):
    litra = 3.785
    return gmaara * litra
gmaara = int(input("Anna gallonat: "))
while gmaara >= 0:
    print(f"Määrä litroina: {muunnos(gmaara)}")
    gmaara = int(input("Anna gallonat: "))
else:
    print("Negatiivinen luku! Hei hei!")


#Tehtävä 7 osa 4

def summailut(kluvut):
    return sum(kluvut)

lista = [1, 33, 2, 984, 1000, 45, 7, 90]
print(summailut(lista))

#Tehtävä 7 osa 5

def summailut1(kluvut1):
    kluvut2 = []
    for numberi in kluvut1:
        if numberi % 2 == 0:
            kluvut2.append(numberi)
    return kluvut2
kluvut1 = [1, 2, 3, 4, 5, 666, 7, 8, 9, 10, 11]
print(summailut1(kluvut1))
print(kluvut1)

#Tehtävä 7 osa 6

def pizza(hinta, halk):
    laskuto = math.pi / 4 * halk **2
    nmetri = laskuto / 10000
    euromaara = hinta / nmetri
    return euromaara

pmaara = int(input("Anna pizzan 1 halkaisija (cm): "))
emaara = int(input("Anna pizzan 1 hinta (€): "))
print(f"{pizza(emaara,pmaara):.2f}€ / mˆ2")

pmaara2 = int(input("Anna pizzan 2 halkaisija (cm): "))
emaara2 = int(input("Anna pizzan 2 hinta (€): "))
print(f"{pizza(emaara2,pmaara2):.2f}€ / mˆ2")

if pizza(emaara,pmaara) > pizza(emaara2,pmaara2):
    print("Pizza 2 on edullisempi vaihtoehto.")
else:
    print("Pizza 1 on edullisempi vaihtoehto.")
