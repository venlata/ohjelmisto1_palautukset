import random
#Ikä, nimi ja tervehdys lisätty peliprojektin ekassa tehtävässä

nimi1 = input("Mikä on nimesi?\n")
ika = int(input("Mikä on ikäsi?\n"))
#Ikälukko lisätty tehtävässä peliprojekti 2 2.9.2026. 
#Tervehdys siirretty lukon jälkeen, pieniä lapsia ei tervehditä.

#inventaario globaali
reppuinventory = []


def komentof1(pvkomento1):
    return "\033[1;31mHyvin tehty!\n\033[0m"
def komentof2(pvkomento2):
    return "\033[1;31m(◕‿-)\n\033[0m"
def komentof5(komento5):
    return "\033[1;31m....\n\033[0m"

while True:
    if ika < 12:
        print("Tänne ei pieniä lapsia haluta! Hyvästi!")
        ika = int(input("Mikä on ikäsi?\n"))
    else:
        print(f"Hei {nimi1}, {ika}v. Tervetuloa ePeliin!\n")
        break

def paavalikko():
    while True:
        print("\033[1;31m(っ◕‿◕)っ PÄÄVALIKKO\n")
        print("Komennot:\n1 = Hyppää kyytiin\n2 = Näytä kieltä\n3 = Lisää tavara reppuun\n4 = Lopeta\n5 = ???\n6 = Tsekkaa repun sisältö")

        komento = input("Anna komento: \033[0m")
        print("\n")

        if komento == "4":
            break

        elif komento == "1":
            print("\033[1;31mHyppäsit!\nHyvin tehty!\n\033[0m")
            k1kys1 = input("Haluaisitko hypätä uudelleen? y/n\n")
            def pvkomento1(k1):
                if k1kys1 == "y":
                    return "Etpä saa.\n"
                elif k1kys1 == "n":
                    return "Hyvä, säästele voimiasi.\n"
            print(pvkomento1(k1kys1))

        elif komento == "2":
            print("\033[1;31m(◕‿-)\nNäytit kieltä. Terveeltä näyttää!\n\033[0m")
            def pvkomento2():
                arvaus1 = int(input("Osaatko arvata mitä lukua ajattelen 1-10 välillä?\n"))
                numero1 = random.randint(1,10)
                while arvaus1 != numero1:
                    print("Ei ollut tuo. Kokeile uudelleen!\n")
                    arvaus1 = int(input("Osaatko arvata mitä lukua ajattelen 1-10 välillä?\n"))
                if arvaus1 == numero1:
                    return "Wau! Arvasit...\n"
            print(pvkomento2())
        elif komento == "3":
            def pvkomento3():
                tavara1 = input("Minkä haluat lisätä reppuun?\nLappu\nEläimen muna\nNukkuva sardiini\n")#tästä olisi hyvä tehdä foolproof myöhemmin ABC-vaihtoehdoin (ei mahdollisuutta syöttää jotain omaa reppuun)
                reppuinventory.append(tavara1)
                return "Hyvä valinta.\n"
            print(pvkomento3())
        elif komento == "6":
            def tulostarep():
                return f"Sinulla on repussasi: {reppuinventory}"
            print(tulostarep)
        else:
            def pvkomento5():
                return "En ymmärrä....\n"
            print(pvkomento5())

def tulostarep():
    return f"Sinulla on repussasi: {reppuinventory}"


paavalikko()

