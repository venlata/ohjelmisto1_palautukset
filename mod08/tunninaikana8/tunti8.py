tup1 = (3, 5, 8, 10, (24, 25), "Moi", 200)

print(len(tup1))
print(tup1.index(10))

if tup1.count(10) == True:
    print("Numero 10 on siellä")
else:
    print("Ei ole 10 siellä")
#TAI lyhyemmin;
print(10 in tup1)

if tup1.count(210) == True:
    print("Numero 210 on siellä")
else:
    print("Ei ole 210 siellä")

tup2 = reversed(tup1)
for tuppeli in tup2:
    print(tuppeli)
# TAI lyhyemmin:
print(tup1[::-1])

#
numbers = {"Viivi": 9999999,
            "Ahmed": 77777777,
            "Pekka": 555555555,
            "George": 333333333}

#Viivin puh nro on xxxxx
#Ahmedin puh nro on xxxxx

for heppu in numbers:
    print(f"{heppu}:n numero on {numbers[heppu]}")

#Kysy kaverin nimi
#jos nimi löytyy, printtaa sen puhelinnumero
#jos ei löydy, printataan että ei löydy

nimi = input("Mikä on kaverin nimi? ")
if nimi in numbers:
    print(f"{nimi}:n numero on {numbers[nimi]}")
else:
    print("Ei ole listassa")

#Tai jos haluat vaan tietää onko nimi listassa:
print(nimi in numbers)

#lista
lista1 = [2, 3, 2, 6, 7, 3, 3]
#halutaan lista joka on vaan [2, 3, 6, 7] eli sama luku vain 1 kertaa listassa
lista2 = set(lista1)
lista3 = list(lista2)
print(lista3)

hedelmat = {"omena", "päärynä", "appelsiini"}
print("omena" in hedelmat)#että onko omena siellä vai ei

students = [{"name": "Ella", "age": 14, "grade": "9"},
            {"name": "Leo", "age": 15, "grade": "8"},
            {"name": "Aino", "age": 14, "grade": "10"}]

print(type(students))
#printataan Ainon arvosana on 10
#index ja key

print(f"{students[2]["name"]}n arvosana on {students[2]["grade"]}")
#Tästä voisi tehdä myös for loop version missä katsotaan kaikkien arvosana
