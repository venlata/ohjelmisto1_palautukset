# while True:
#     try:
#         luku = int(input("Anna luku: "))
#     except ValueError as e:
#         print("Hyi! Anna numero!!!")
#     else:
#         print(f"Kiitos luvusta {luku}")
#         break


# l1 = [1, 2, 3, 4]
# try:
#     l1[6]
# except:
#     print("Moi")

# try:
#     1 / 0
# except ZeroDivisionError as e:
#     print(type(e))
#     print("Jotain meni pieleen")

#import random
# person = random.choice(["A", "B", "C", "D", "E", "F"])
# print(person)

# di1 = {"a" : 1, "b" : 45, "c" : 5}
# set1 = {2, 4, 6, 8}

# for item in set1:
#     print(item)

# for item in di1:
#     print(item, di1[item])

# import tehtava11julkaisut
# print(tehtava11julkaisut.kir1.nimi)

class Biisi:
    def __init__(self, laulaja, biisinimi):
        self.laulaja = laulaja
        self.biisinimi = biisinimi

b1 = Biisi("laulaja 1", "biisi1")
b2 = Biisi("laulaja 2", "biisi2")
b3 = Biisi("laulaja 3", "biisi3")
b4 = Biisi("laulaja 4", "biisi4")
b5 = Biisi("laulaja 5", "biisi5")
b6 = Biisi("laulaja 6", "biisi6")

blista = [b1, b2, b3]

for i in blista:
    print(i.laulaja)

class Playlist:
    def __init__(self):
        self.munlista = []

    def lisaa(self, biisi):
        self.munlista.append(biisi)

pl1 = Playlist()
pl2 = Playlist()

pl1.lisaa(b1)
pl1.lisaa(b4)

pl2.lisaa(b3)
pl2.lisaa(b6)
pl2.lisaa(b5)

for i in pl1.munlista:
    print(i.biisinimi)

for i in pl2.munlista:
    print(i.biisinimi)


