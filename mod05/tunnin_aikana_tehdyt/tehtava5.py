#Tehtävä 5 / mod05
#Tehtävä 5, osa 1:
import random
def t5o1():
    lukuni = 0
    while lukuni <= 1000:
        print(lukuni)
        lukuni += 3

#Tehtävä 5, osa 2
def t5o2():
    tuuma = 2.54
    vastahus = float(input("Anna tuumat niin käännetään senttimetreiksi: "))
    while vastahus > 0:
        print(f"{(vastahus) * (tuuma):.2f} senttimetreissä")
        vastahus = float(input("Anna tuumat niin käännetään senttimetreiksi: "))
    else:
        print("Älä anna negatiivisia lukuja :()")


#Tehtävä 5, osa 3
def t5o3():
    luvut = []
    pienin = None
    isoin = None
    while True:
        luku = input("Syötä luku: ")
        if luku == "":
            break
        luku = int(luku)
        luvut.append(luku)
        if pienin is None or luku < pienin:
            pienin = luku
        if isoin is None or luku > isoin:
            isoin = luku
    print(f"Tässä pienin luku: {pienin}\nTässä isoin luku: {isoin}")

#Luulin pitkään ettei tää toimi ja lisäsin ja poistin osioita koska unohin lisätä t5o3 sulut :D 
#Kunnes kokeilin Thonnyn kautta myös

#Tehtävä 5 osa 4
def t5o4():

    kokluku = random.randint(1, 10)

    while True:
        arvaus = input("Arvaa luku: ")
        arvaus = int(arvaus)

        if arvaus == kokluku:
            print("Oikein")
            break

        if arvaus < kokluku:
            print("Liian pieni arvaus")

        if arvaus > kokluku:
            print("Liian suuri arvaus")


#Tehtävä 5 osa 5
def t5o5():
    
    tunnari = "python"
    passu = "rules"
    maximit = 5
    yritykset = 0

    while yritykset <= maximit:
    #for yritys in range(0, maximit):

        stunnus = input("Syötä käyttäjätunnus: ")
        spassu = input("Syötä salasana: ")
        yritykset += 1
        if stunnus == tunnari and spassu == passu:
            print("Tervetuloa")
            break
        if yritykset >= maximit:
            print("Pääsy evätty")
            break

