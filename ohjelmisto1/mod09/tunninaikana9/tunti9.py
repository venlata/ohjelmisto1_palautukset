#Tunti 9 harjoitustehtävät
#Luokat ja oliot

class Rectangle:
    def __init__(self, width, height):#tässä määritellään ominaisuudet mitä oliolla voi olla, vaikka ikä jne
        self.width = width
        self.height = height
    def circumference(self):
        print(2 * (self.width + self.height))
    
    
r1 = Rectangle(45, 35)
r2 = Rectangle(22, 33)

# r1.circumference()
# r2.circumference()

class Person:
    def __init__(self, name, age):
        self.name = name
        #self.surname = surname
        self.age = age
    def walk(self):#metodi, eli jokin tekeminen
        print(f"{self.name} kävelee 🤠'")
    def adult(self):
        if self.age >= 18:
            print(f"{self.name} on aikuinen")
        else:
            print(f"{self.name} ei ole aikuinen")


p1 = Person("Jaska", 99)
p2 = Person("Maija", 44)
p3 = Person("Kerkko", 11)

# p1.walk()
# p1.adult()
# p3.adult()

class Book:
    def __init__(self, writer, title, pages=100):
        self.writer = writer
        self.title = title
        self.pages = pages
        
        
    

b1 = Book("Kalle Kirjailijainen", "Ensimmäinen kirjani", 135)
b2 = Book("Kaija Kirjoittaja", "Parempi kirja kuin Kallen", 666)
b3 = Book("Matti", "Matin muistelmat", 33)
b4 = Book("Rouva Kirjailija", "Kirja nro 7")
# print(b2.pages)
# print(b4.pages)

class Ope:
    def __init__(self, name):
        self.name = name
    def mystu(self, opis):
        print(f"Minä olen {self.name} ja {opis.name} on mun opiskelija")


class Opiskelija:
    def __init__(self, name):
        self.name = name

op1 = Ope("Piia")
opis1 = Opiskelija("Kalle")
op2 = Ope("Ulla")
opis2 = Opiskelija("Jorma")
opis3 = Opiskelija("Kerttu")

# op1.mystu(opis1)
# op2.mystu(opis3)


class Kirjailija:
    def __init__(self, nimi):
        self.nimi = nimi

lija1 = Kirjailija("Martta Meikäläinen") #Kirjailija puuttui aluks alusta, tää oli pelkkä tavallinen muuttuja :D
lija2 = Kirjailija("Kerttu Kurttunen")


class Kirja:
    def __init__(self, knimi, kirjailija):
        self.nimi = knimi
        self.kirjailija = kirjailija

kirja1 = Kirja("Kirja 1", lija1.nimi)
kirja2 = Kirja("Kirja 2", lija2.nimi)

print(f"Kirjan nimi: {kirja1.nimi}, Kirjailija: {kirja1.kirjailija}")
print(f"Kirjan nimi: {kirja2.nimi}, Kirjailija: {kirja2.kirjailija}")

class Asukas:
    def __init__(self, nimi):
        self.nimi = nimi

a1 = Asukas("Hessu")
a2 = Asukas("George")
a3 = Asukas("Liina")

class Kaupunki:
    def __init__(self, nimi, asukas):
        self.nimi = nimi
        self.asukas = asukas
    def kuka(self):
        print(f"{self.asukas} asuu kaupungissa {self.nimi}")

k1 = Kaupunki("Oulu", a2.nimi)
k2 = Kaupunki("Pariisi", a1.nimi)

# print(f"{k1.asukas} asuu {k1.nimi}ssa")
# print(f"{k2.asukas} asuu {k2.nimi}ssa")
k1.kuka()
lista1 = [a1, a2, a3]

for asukas in lista1:
    print(asukas.nimi)

#t1 tunnilla:
#class Tilillä property saldo, metodit talletus ja nosto
#voit tallettaa rahaa, nostaa rahaa, ja katsoa saldon määrän
#Pohjasaldo vaikka 100€

class Tili:
    def __init__(self, saldo):
        self.saldo = saldo
    def talletus(self, tmaara):
        self.saldo = self.saldo + tmaara
    def nosto(self, nmaara):
        self.saldo = self.saldo - nmaara

tili1 = Tili(100)

while True:
    kys1 = input("Mitä haluat tehdä?\nA = Talleta rahaa\nB = Nosta rahaa\nC = Tarkasta saldo\n")
    if kys1 == "A":
        talle = int(input("Paljonko talletetaan: "))
        tili1.talletus(talle)
    if kys1 == "B":
        nost = int(input("Paljonko nostetaan: "))
        tili1.nosto(nost)
    if kys1 == "C":
        print(f"Saldosi on {tili1.saldo}")
        break

class Kirja1:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirjasto:
    def __init__(self, nimi):
        self.nimi = nimi
        self.kirjat = []
    def lisays(self, krja):
        self.kirjat.append(krja)

kr1 = Kirja1("Hevoskirja 1")
kr2 = Kirja1("Aasit 2")
kr3 = Kirja1("Aapinen")
kr4 = Kirja1("Raamattu")
krjasto1 = Kirjasto("Oodi")

krjasto1.lisays(kr1.nimi)
krjasto1.lisays(kr2.nimi)
print(krjasto1.kirjat)
for kirjuli in krjasto1.kirjat:
    print(kirjuli)