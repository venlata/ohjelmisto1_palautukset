# #Tunti 6 harjoitukset

# #Ohjelma joka printtaa parilliset luvut 20-0, while loopilla
# # luku1 = 20

# while True:
#     if luku1 % 2 == 0:
#         print(luku1)

#     luku1 -= 1
#     if luku1 <= 0:
#         break

# #Voi tehdä myös näin päin:

# luku2 = 20

# while luku2 >= 0:
#     if luku2 % 2 == 0:
#         print(luku2)
#     luku2 -= 1

# #Ohjelma kysyy "Mikä on sinun nimesi?" niin kauan kun et paina välilyöntiä
# #kun painat välilyöntiä ohjelma lopettaa

# nimi1 = input("Mikä on nimesi? ")
# while nimi1 != ' ':
#     nimi1 = input("Mikä on nimesi? ")

# #Jos haluaa taas että Enter päättää loopin, pyyhi vain välilyönti pois (rivi 27)

# #Section1

# names1 = ['Alice', 'Bob', 'Carmen', 'David', 'Eve', 'Fred', 'George', 'Harry', 'Ivy', 'Jill']
# #Voit tsekkaa että tämän tyyppi on lista: print(type(names1))
# #Ensimmäinen listassa on aina 0.
# #Näin printtaat jonkun jonosta:
# print(names1[4])
# #Viimesen jäsenen saa tällä:
# print(names1[-1])

# #Slicing:
# #start(including):end(excluding):step
# print(names1[2:8:2])
# #Jos haluat default hypyt (1), voit ottaa stepin pois:
# print(names1[2:5])
# #Default aloituskohta on myös 0, eli jos haluaa siitä aloittaa voi jättää startin pois:
# print(names1[:5])
# #Lopun default on vaan loppuun asti:
# print(names1[5:])
# #Huolimatta onko miinusluku siellä:
# print(names1[-3:])
# #Voi listata myös taaksepäin listalla:
# print(names1[4:0:-1])
# #Näin saa kaikki alusta loppuun:
# print(names1[::])
# #Toisin päin:
# print(names1[::-1])

# #Voit lisätä listaan tavaraa appendilla:

# fruits = ["apple", "banana", "cherry", "apple"]
# print(id[fruits])

# fruits.append("orange")
# fruits.append("plum")

# print(fruits)
# print(id[fruits])

# #Voit muuttaa muuttujan, myös muistipaikka vaihtuu silloin:
# Ylempänä sitä ei tapahdu koska kyseessä on lista, se vaan päivittyy
# x = 2
# print(id(x))
# x = 3
# print(id(x))

# numerot = [3, 5, 10, 9]

# #Onko alkio listassa:
# if 10 in numerot:
#     print("On se siellä")
# else:
#     print("Ei löydy")

# #Monentenako alkio on listassa:
# mones = numerot.index(9)
# print(mones)

# #Tiettyyn kohtaan alkion lisääminen:
# numerot.insert(1, 6)
# print(numerot)

# #Voit lisätä listaan myös listan sisään:
# # numerot.insert(2, [2, 8])
# # print(numerot)
# # print(numerot[2])

# #listan pituus:
# print(len(numerot))

# print(numerot[len(numerot)-1])

# #Usean alkion lisääminen:
# uudetnumerot = [33, 40]
# numerot.extend(uudetnumerot)
# print(numerot)

# #Järjestykseen:
# numerot.sort()
# #ei toimi jos ei ole homogeeninen lista

# #For:
# for lukunen in numerot:
#     print(lukunen)
#     print("jee")
# print("ok")

# #Uusi lista aiemman olemassaolleen listan perusteella:
# lista2 = []
# for lukunen1 in numerot:
#     lista2.append(lukunen1 * 2)
# print(lista2)

# #Ohjelma kysyy kaverien nimet
# #Niin kauan kun vastaat, nimet kerätään listaan
# #Kun vastaat välilyönnillä, ohjelma loppuu
# nimet3 = []
# kysmys = input("Anna kaverin nimi: ")
# while kysmys != " ":
#     nimet3.append(kysmys)
#     kysmys = input("Anna kaverin nimi: ")
# print(nimet3)

# #Tai näin:
# plista = []
# while True:
#     nimmi = input("anna nimi: ")
#     if nimmi == " ":
#         break
#     else:
#         plista.append(nimmi)
# print(f"Tässä lista: {plista}")

# #Tehtävä, jos kaverin nimi on 6 merkkiä tai enemmän, se ei kelpaa listaan:
# mlista = []

# while True:
#     nimi666 = input("Anna nimi: ")
#     pituus1 = len(nimi666)
#     if nimi666 == " ":
#         break
#     if pituus1 >= 6:
#         mlista.append(nimi666)
# print(f"Nimet: {mlista}")

# #Range
# #range(start(including), end(excluding), step)

# for item in range(0, 51, 2):
#     print(item)

# #Samalle riville:
# listing = []
# for numba in range(11):
#     listing.append(numba ** 2)
# print(listing)

