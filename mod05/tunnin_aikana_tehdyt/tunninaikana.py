#Tunti 5, mod05
import time
import random
def osa1():
    #Muuttujalla voi olla useampi "nimi"
    muut1 = muut2 = str("lopullinen muuttuja")
    print(muut1)
    print(muut2)
    #ja ne voi vaihtaa päittäin:
    muut3 = 67
    muut4 = 56
    print (muut3)
    muut3, muut4 = muut4, muut3
#
def osa2():
    #tämä printtaa objektin "koon"
    stri1 = 'hello world'
    print(len(stri1))
    #jos muuttujaan tehdään muutoksia, ne muuttaa muuttujaa :D
    a1 = 5
    b1 = 7
    a1 = a1 + 1
    print(a1)
    #tällä miinustetaan tuosta 1:
    a1 -= 1
    print(a1)
    #tällä lisätään:
    a1 += 8
    print(a1)
    #kerrotaan:
    a1 *= 3
    print(a1)

def osa3():
    #Toistorakenteet, while
    #while menee loputtomaan looppiin ellei muuttujalle anna jotain mikä muuttaa sen arvoa, kts rivi kerta += 1
    kerta = 0.8
    while kerta < 5:
        print("Hello")
        kerta += 1
    kerta1 = 1
    while kerta1 <= 5:
        print("Hey")
        kerta1 += 1
    
    
def osa4():
    #printtaa kaikki luvut 1-20 parittomat:
    luku = 1
    while luku <= 20:
        print(luku)
        luku += 2
    #parilliset:
    luku2 = 1
    while luku2 <= 20:
        if luku2 % 2 == 0:
            print(luku2)
            luku2 += 1
    
    
def osa5():
    #Kysy luku, positiivinen, kokonaisluku. Lähtölaskenta luvusta nollaan ja sitten Kaboom
    #bonusta jos saa ajastuksen, sekunti per numero
    luku5 = int(input("Anna luku:\n"))
    while luku5 > 0:
        print(luku5)
        luku5 -= 1
    print("Kaboom!")

def osa6():
    #Anna salasana > oikein > Pääsy annettu, väärin > Väärä salasana, kokeile uudelleen
    password = "dabomb"
    psw2 = "theebomb"
    salsana = input("Anna salasana:\n")
    while salsana != password or psw2:
        print("Väärä salasana, kokeile uudelleen")
        salsana = input ("Anna salasana:")
        if salsana == password:
            print("Pääsy annettu, laitoit salasanaksi dabomb")
            break
        if salsana == psw2:
            print("Laitoit salasanaksi theebomb")
            break
    

def osa7():
    #import random lisätty filun alkuun
    #tämän voisi tehdä kahdella iffillä, mutta se kuluttaa enemmän resursseja
    muut = 0
    while muut <= 10:
        noppa = random.randint(1, 2)
        if noppa != 1:
            print("sait kruunan")
        elif noppa == 1:
            print("sait klaavan")
        muut += 1
    print("Heitit kolikkoa 10 kertaa")

def osa8():
    #nopanheittoa kahdella nopalla kunnes tulee 1 ja 3!
    #sitten se printtaa Nyt tuli 1 ja 3, jatketaan
    #sitten
    #Nyt tuli 2 ja 2, jatketaan
    #sitten
    #Nyt tuli 3 ja 3, jee!
    # while True:
    #     noppa1 = random.randint(1, 3)
    #     noppa2 = random.randint(1, 3)
    #     tulos = (noppa1, noppa2)

    #     jackpot1 = (noppa1 == 1, noppa2 == 3)
    #     jackpot2 = (noppa1 == 2, noppa2 == 2)
    #     jackpot3 = (noppa1 == 3, noppa2 == 3)
    #     if tulos == (True, True):
    #         print ("Tuli 1 ja 3, jatketaan.")
    #     elif tulos == (False, False) and (noppa1 == 2 and noppa2 == 2):
    #         print("Tuli 2 ja 2, jatketaan!")
    #     elif tulos == (noppa1 == 3, noppa2 == 3):
    #         print("Tuli 3 ja 3, hienoa!")
    #         break
    #     else:
    #         print("Jatketaan..")
    # while True:
    #     noppa1 = random.randint(1, 3)
    #     noppa2 = random.randint(1, 3)
    #     tulos = (noppa1, noppa2)

    #     if tulos == (1, 3):
    #         print("Tuli 1 ja 3, jatketaan.")
    #     else:
    #         print("Jatketaan")
    #         if tulos == (2, 2):
    #             print("Tuli 2 ja 2, jatketaan!")
    #         else:
    #             print("Jatketaan..")
    #             if tulos == (3, 3):
    #                 print("Tuli 3 ja 3, hienoa!")
    #                 break
    state = 0

    while True:
        noppa1 = random.randint(1, 3)
        noppa2 = random.randint(1, 3)
        tulos = (noppa1, noppa2)

        if state == 0:
            if tulos == (1, 3):
                print("Tuli 1 ja 3, jatketaan.")
                state = 1
            else:
                print("Jatketaan")

        elif state == 1:
            if tulos == (2, 2):
                print("Tuli 2 ja 2, jatketaan!")
                state = 2
            else:
                print("Jatketaan.")

        elif state == 2:
            if tulos == (3, 3):
                print("Tuli 3 ja 3, hienoa!")
                break
            else:
                print("Jatketaan..")
        
#Jeesus että kesti kauan
        
        

osa8()     