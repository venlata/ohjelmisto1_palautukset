import math
num = math.pi
print(f"{num:10.2f}")
#10 tuossa on kentän leveys (merkkiä), 2 montako desimaalia saa olla

nom = "jee"
print(f"{nom:>10s}")
#tuolla saa stringin merkkikenttään lisää leveyttä. > meinaa kumpaan suuntaan tekstiä työnnetään

num1 = 200
print(f"{num1:10d}")
#d == digits (kokonaisluvuille)

#and tulee aina ennen or jos molemmat on yhdessä:
print(True or True and False)
#eli tästä tulee True

#mutta not tulee ennen and:
print(not True and False)
#Eli tästä tulee False

#Funktioon voi syöttää erilaisia tyyppejä:
def funk1(x, y):
    z = x + y
    return z
print(funk1([44, 7, 90], [33, 25]))
print(funk1(33, 44))
print(funk1("Jee"," Joo"))

#Voit myös esisyöttää funktioon tiedot:
def funk2(o=55, k=77):
    e = o + k
    return e
print(funk2())#Printtaa funktion oletusarvon (eli nyt se mitä syötettiin ensin jo funktioon)
print(funk2(99, 111))#Tässä syötettiin uudet arvot funktioon

#Myös for loopista voi paeta:
for numba in range(10):
    print(numba)
    if numba == 5:
        break
#Jos break on printtiaktion jälkeen, break tapahtuu vasta kun numero on jo printattu ^
#Jos breakin laittaa ennen printtausta, jono katkeaa jo siihen määrättyyn numeroon:
for numba in range(10):
    if numba == 5:
        break
    print(numba)

eka = 1
while eka <= 3:
    toka = 1
    while toka <= 3:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1

#Voit laittaa ei-kiinteän määrän argumentteja (*args):
def funk3(*args):
    for item in args:
        print(item)

funk3(2, 6, 8, 10, 4)

#