import math
# \t = tab, \n = new tab
print("Hello!\t\tWhat's up?")
print("Hello!\nWhat is up?")
#Testailut tunnin aikana
print('"What?", she said')
nimi = input ("Nimeni on ")
print("Hei," + nimi + "!\N{grinning face with smiling eyes}")
vastaus = input("Meneekö hyvin?\n")
print(vastaus)
#Ylempään voisi myös laittaa yes/no vaihtoehdot
#tyyppejä:
lukupi = 3.14159
sade = 4
uusiluku = 3.0
lukuyksi = 2
lukukaksi = "2"
lukukolme = '3'
booli = True
#Tämä laskee ympyrän piirin:
print("\nYmpyrän piiri on: ")
print(2*lukupi*sade)
#Seuraava laskee pinta-alan:
print("\nYmpyrän pinta-ala on: ")
print(sade*sade*lukupi)
print("\n")
#Miten löytää lukupi:
print(id(lukupi))
print("\n")
#Voi tehdä myös näin löytääksesi pi:n:
print(math.pi)
print("\n")
#Tähän ylempään liittyen: import math laitetaan aina tiedoston alkuun!!!
#Näin voi tarkastaa objektin tyypin:
print(type(sade))
print(type(lukupi))
print(type(uusiluku))
print(type(nimi))
print(type(lukuyksi))
print(type(lukukaksi))
print(type(lukukolme))
print(type(booli))
#Laskutoimituksia voi tehdä kun objektin tyyppi on joku luku eikä string tai boolean arvo:
#plussa:
print(lukuyksi + 3)
#kerto:
print(uusiluku * 3)
#jako:
print(lukupi / 2)
#potenssi:
print(lukuyksi ** 6)
#Huom. vastaus riippuu annetun luvun tyypistä, onko float vai int jne
#Myös string objekteja voi "laskea yhteen" jne, lopputulos vain on 2 objektia ns. liimattuna yhteen
print(lukukolme + lukukaksi)
