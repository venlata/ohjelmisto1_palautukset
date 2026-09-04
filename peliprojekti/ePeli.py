
#Ikä, nimi ja tervehdys lisätty peliprojektin ekassa tehtävässä

nimi1 = input("Mikä on nimesi?\n")
ika = int(input("Mikä on ikäsi?\n"))
#Ikälukko lisätty tehtävässä peliprojekti 2 2.9.2026. 
#Tervehdys siirtyy lukon jälkeen, pieniä lapsia ei tervehditä.

while True:
    if ika < 12:
        print("Tänne ei lapsia haluta! Hyvästi!")
        break
    if ika >= 12:
        print(f"Hei {nimi1}, {ika}v. Tervetuloa ePeliin!\n")
        while ika >= 12:
            print("\033[1;31m(っ◕‿◕)っ PÄÄVALIKKO\n")

            komento = input("Anna komento: \033[0m")
            print("\n")

            if komento == "lopeta":
                break

            elif komento == "olen iloinen":
                print("Erikoista!\n")
            elif komento == ":p":
                print("(◕‿-)\n")
    break

