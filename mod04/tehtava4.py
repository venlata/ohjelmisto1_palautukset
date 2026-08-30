def teht4_1():
    #Tehtävä 4 osa 1
    kuha = int(input("Kerro kuhasi pituus (cm):\n"))
    if kuha < 37:
        print(f"Kuhasi on alamittainen {37 - (kuha)} senttimetrillä. Laske se heti menemään!")
    else:
        print("Ihan hieno kuha, saat pitää sen.")

def teht4_2():
    #Tehtävä 4 osa 2
    v1 = str("LUX")
    v2 = str("A")
    v3 = str("B")
    v4 = str("C")
    hytti = input(f"Mikä näistä on hyttiluokkasi: {v1, v2, v3, v4}?:\n")
    if hytti == v1:
        print("LUX on parvekkeellinen hytti yläkannella.\n")
    elif hytti == v2:
        print("A on ikkunallinen hytti autokannen yläpuolella.\n")
    elif hytti == v3:
        print("B on ikkunaton hytti autokannen yläpuolella.\n")
    elif hytti == v4:
        print("C on ikkunaton hytti autokannen alapuolella.\n")
    else:
        print("Virheellinen hyttiluokka\n")

def teht4_3():
    #Tehtävä 4 osa 3
    m = str("mies")
    n = str("nainen")
    suku = input("Kerro biologinen sukupuolesi, " + m + " tai " + n + ":\n")
    hemo = int(input("Kerro hemoglobiiniarvosi:\n"))
    if suku == m and 195 >= hemo >= 134:
        print("Hemoglobiinisi on normaali.\n")
    elif suku == m and hemo > 195:
        print("Hemoglobiinisi on liian korkealla.\n")
    elif suku == m and hemo < 134:
        print("Hemoglobiinisi on liian alhainen.\n")
    elif suku == n and 175 >= hemo >= 117:
        print ("Hemoglobiinisi on normaali.\n")
    elif suku == n and hemo > 175:
        print("Hemoglobiinisi on liian korkea.\n")
    elif suku == n and hemo < 117:
        print("Hemoglobiinisi on liian alhainen.\n")
#Tuon olisi voinut toki tehdä myös kahden iffin alle (nainen -> hemoblogiinioptiot & mies -> hemoglobiinioptiot)

def teht4_4():
    #Tehtävä 4 osa 4
    kvuosi = int(input("Anna vuosi:\n"))
    if kvuosi % 4 == 0:
        print("Se on karkausvuosi!\n")
    else:
        print("Se ei ole karkausvuosi.\n")

