
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
            print("Komennot:\nHypi\nNäytä kieltä\n???\nLopeta\n")

            komento = input("Anna komento: \033[0m")
            print("\n")

            if komento == "Lopeta":
                break

            elif komento == "Hypi":
                print("Hyvin tehty!\n")
            elif komento == "Näytä kieltä":
                print("(◕‿-)\n")
    break

