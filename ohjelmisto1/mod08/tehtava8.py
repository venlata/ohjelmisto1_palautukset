
#Tehtävä 8 osa 1

kauet = (0,"tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")
kysmys = int(input("Anna kuukauden numero (1-12): "))

if kysmys == 1 or kysmys == 2 or kysmys == 12:
    print(f"{kysmys}. kuukausi {kauet[kysmys]} on talvella")
if kysmys == 3 or kysmys == 4 or kysmys == 5:
    print(f"{kysmys}. kuukausi {kauet[kysmys]} on keväällä")
if kysmys ==  6 or kysmys == 7 or kysmys == 8:
    print(f"{kysmys}. kuukausi {kauet[kysmys]} on kesällä")
if kysmys == 9 or kysmys == 10 or kysmys == 11:
    print(f"{kysmys}. kuukausi {kauet[kysmys]} on syksyllä")
#Tää ei nyt todennäköisesti ole mitä haettiin mutta tämän saat :D

#Tehtävä 8 osa 2

nimet = set()
nimi = input("Anna nimi: ")
while nimi != "":
    nimet.add(nimi)
    nimi = input("Anna nimi: ")
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi!")
    
for yks in nimet:
    print(yks)

#Tehtävä 8 osa 3

lentoasemat = {"AGAR": "Ulawa airport",
               "FACK": "Christiana Airport",
               "FIMA": "Agalega Airstrip",
               "EEKU": "Kihnu Airfield",
               "EFRA": "Rautavaara Airfield",
               "EFOU": "Oulu Airport"}

while True:
    valinta = input("Mitä haluat tehdä?\nA = Syötä uusi lentoasema\nB = Hae jo syötetyn lentoaseman tiedot\nC = Lopeta\n") 
    while valinta != "C":

        if valinta == "A":
            uusicao = input("Anna uuden aseman ICAO-koodi: ")
            uusasema = input("Anna uuden aseman nimi: ")
            lentoasemat[uusicao] = uusasema
            break

        elif valinta == "B":
            annaicao = input("Anna aseman ICAO-koodi: ")
            print(lentoasemat[annaicao])
            break
    if valinta == "C":
        break
