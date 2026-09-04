##Tunti 6 harjoitukset

##Ohjelma joka printtaa parilliset luvut 20-0, while loopilla
## luku1 = 20

# while True:
#     if luku1 % 2 == 0:
#         print(luku1)

#     luku1 -= 1
#     if luku1 <= 0:
#         break

##Voi tehdä myös näin päin:

# luku2 = 20

# while luku2 >= 0:
#     if luku2 % 2 == 0:
#         print(luku2)
#     luku2 -= 1

##Ohjelma kysyy "Mikä on sinun nimesi?" niin kauan kun et paina välilyöntiä
##kun painat välilyöntiä ohjelma lopettaa

# nimi1 = input("Mikä on nimesi? ")
# while nimi1 != ' ':
#     nimi1 = input("Mikä on nimesi? ")

##Jos haluaa taas että Enter päättää loopin, pyyhi vain välilyönti pois (rivi 27)

##Section1

names1 = ['Alice', 'Bob', 'Carmen', 'David', 'Eve', 'Fred', 'George', 'Harry', 'Ivy', 'Jill']
#Voit tsekkaa että tämän tyyppi on lista: print(type(names1))
#Näin printtaat jonkun jonosta:
print(names1[4])
