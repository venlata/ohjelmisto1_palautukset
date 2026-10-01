import random

inventory_backpack = []
mayorpoints = 0

class Player:
    def __init__(self, name, age, inventory, currentroom, pmayorpoints):
        self.name = name
        self.age = age
        self.inventory = inventory
        self.currentroom = currentroom
        self.mayorpoints = pmayorpoints
    def move(self, room):
        self.currentroom = room.name
    def collectitem(self, item):
        inventory_backpack.append(item)
    def loseitem(self, item):
        inventory_backpack.remove(item)
    def itemlist(self):
        for i in self.inventory:
            print(i.name)
    

class Room:
    def __init__(self, name, item=None):
        self.name = name
        self.item = item

class Item:
    def __init__(self, name, weight=10):
        self.name = name
        self.weight = weight #weight in grams

playername = input("Mikä on nimesi?\n")
playerage = int(input("Mikä on ikäsi?\n"))

room1 = Room("Sardiinian Kaupungintalo")
room2a = Room("Pub Sihisevä Sardiini", "Rätti")
room2b = Room("Seppo Sardiinin koti")
room3a1 = Room("Baarin henkilökunnan huone")
room3a2 = Room("Baarin vessa")
room3b1 = Room("Sepon pihavaja")
room3b2 = Room("Sepon pihavajan ullakko")
room4a = Room("Sardiini highway")
room4b = Room("Levämetsä")
room5 = Room("Maurin uusi pesä")
room6a = Room("Epäonnistumisen tyyssija")
room6b = Room("Hyvä ratkaisu")

sanakirja = Item("Sanakirja", 20)
pesis = Item("Pesäpallomaila", 200)
avain = Item("Avain", 4)
ratti = Item("Rätti", 3)
juoma = Item("Juomapullo")

while True:
    if playerage < 12:
        print("Annoitko ikäsi vahingossa planktonvuosissa vai oletko vain noin nuori??? Tänne ei pieniä lapsia haluta!")
        playerage = int(input("Mikä on ikäsi?\n"))
    else:
        player1 = Player(playername, playerage, inventory_backpack, room1.name, mayorpoints)
        print(f"Hei {playername}, {playerage}v. Tervetuloa Sardiiniaan!\nOlet nyt muikku, ja paikassa {player1.currentroom}\n.")
        break

def meetthemayor():
    print("Sardiinian pormestari tervehtii sinua.\nPORMESTARI: 'Hauska tavata. Olen hukannut lemmikkikatkarapuni Maurin, ja tarvitsen apua sen löytämiseen.\nOlisitko sinä tullut etsimään kanssani?'")
    hellomayor = input("A = Tervehdi pormestaria kuin normaali muikku ja lupaa auttavasi parhaan mukaan\nB = Sylkäise maahan ja nyökkää pormestarille\nC = Kumarra syvään ja sano 'Oi rouva pormestari; vannon sinulle uskollisuuteni'\n")
    def maya():
        player1.mayorpoints += random.randint(2,4)
        return "Pormestari kiittää sinua. Voit erottaa hänen silmäkulmastaan helpotuksen kyyneleen."
    def mayb():
        player1.mayorpoints += 1
        return "Pormestari vilkaisee sinua kauhuissaan, mutta hyväksyy vastauksen hiljaa nyökäten. Kaikki apu on tarpeen."
    def mayc():
        player1.mayorpoints -= 1
        return "Pormestaria näkyvästi etoo limainen käytöksesi.\nPORMESTARI: 'Olet melko erikoinen, mutta apusi on silti tarpeen...'"
    while True:
        if hellomayor == "A":
            maya()
            break
        elif hellomayor == "B":
            mayb()
            break
        elif hellomayor == "C":
            mayc()
            break
        else:
            print("Vastaa vain A, B, tai C.")

def mainmenu():
    print("PORMESTARI: 'Voit valita yhden tavaran mukaan kaupungintalon vitriinistä. Toivon mukaan siitä on meille apua.'\n")
    firstitem = input("Valitse hyllyltä yksi (1) esine:\nA = Sardiini - Katkarapu -sanakirja\nB = Pesäpallomaila (muikulle sopivan kokoinen)\nC = Avain\n")
    if firstitem == "A":
        inventory_backpack.append(sanakirja)
    elif firstitem == "B":
        inventory_backpack.append(pesis)
    elif firstitem == "C":
        inventory_backpack.append(avain)
    else:
        print("Tuo ei ollu A, B, tai C. Et saa mitään.")
    print("Hyvä. Pääsette aloittamaan matkanne. Tie erkanee kahteen suuntaan.\nTie A näkyy johtavan... kohti juottolaa? Tie B taas vie jonkun kotipihaan.")
    crossing()

def crossing():
    while True:
        crossing1 = input("Haluatko tien A vai B?\n")
        if crossing1 == "A":
            player1.move(room2a)
            break
        elif crossing1 == "B":
            player1.move(room2b)
            break
        else:
            crossing1 = input("Niin siis A vai B?\n")

def room2afun():
    print(f"Saavutte paikkaan {player1.currentroom}. Pormestari kavahtaa paikan hajua.\nPaikan kanta-asiakas nappaa tiskiltä rätin ja heittää sinua sillä. Saat kopin.\nBaarimikko nauraa räkäisesti tapahtuneelle.")
    inventory_backpack.append(ratti)
    print("BAARIMIKKO: 'Tervetuloa Sihisevään Sardiiniin. Haluatteko juotavaa?'\nPORMESTARI: 'Ei missään nimessä. Etsimme kadonnutta katkarapuani Mauria. Onko täällä näkynyt?'")
    print("BAARIMIKKO: 'En ehdi katselemaan sellaisia työn ohella, mutta voitte itse tutkia pubini paikat jos haluatte.'")
    while True:
        crossing2a = ("Pormestari vilkaisee ensin Baarimikkoa epäilevästi, ja sitten osoittaa kahta ovea baarin takaseinustalla.\nOtatko oven A vai B?")
        if crossing2a == "A":
            player1.move(room3a1)
            room3a1fun()
            break
        elif crossing2a == "B":
            player1.move(room3a2)
            room3a2fun()
            break
        else:
            crossing2a = input("Tuo ei ole A tai B. Valitse A tai B")

def room3a1fun():
    print(f"Saavutte paikkaan {player1.currentroom}.\nHuone näyttää pölyiseltä, mutta muuten siistiltä.")
    useitemratti = input("Mauria ei näy huoneessa, mutta sinulla on tilaisuus tehdä hyvä teko ja pyyhkiä rätillä pölyjä pois.\nKäytätkö rättiä?\nA = Kyllä\nB = Ei")
    while True:
        if useitemratti == "A":
            inventory_backpack.remove(ratti)
            mayorpoints += 4
            print("PORMESTARI: 'Olipa mukavasti tehty.")
            break
        elif useitemratti == "B":
            break
        else:
            useitemratti = input("Valitse A tai B.")
    print("Aika lähteä, Mauri ei ole täällä. Huoneessa on takaovi, josta Pormestari jo sujahtaa ulos.")
    player1.move(room4a)
    room4afun()

def room3a2fun():
    print(f"Saavutte paikkaan {player1.currentroom}. Mauria ei näy, mutta nurkassa kyhjöttää pieni surkea sardiini lian peitossa.\nNURKKASARDIINI: 'Tulitteko tekin pilkkaamaan minua? Nuoret sardiinit heittivät päälleni jotain tuosta lattialta enkä uskalla poistua...'")
    useitemratti2 = ("Pormestarilla on tippa silmäkulmassa. Liikuttaako sinuakin Nurkkasardiinin huono kohtelu?\nKäytätkö rättiä hänen putsaamiseensa?\nA = Kyllä\nB = Ei")
    while True:
        if useitemratti2 == "A":
            inventory_backpack.remove(ratti)
            mayorpoints += 5
            print("NURKKASARDIINI: 'Kiitos! Kiitos tuhannesti!'")
            break
        elif useitemratti2 == "B":
            mayorpoints -= 2
            ("Oletpas pihi kun et rättiä viitsi käyttää!")
            break
        else:
            useitemratti2 = ("Valitse A tai B!")
    print("Aika lähteä, Mauri ei ole täällä. Pormestari ryömii jo ulos vessan ikkunasta kohti levämetsää.")
    player1.move(room4b)
    

def room4afun():
    print(f"Saavutte paikkaan {player1.currentroom}. Edessä aukeaa tie, joka johtaa vain yhteen suuntaan.")
    if mayorpoints >= 0:
        joke = input("Pormestari vaikuttaa jo kyllästyneen seuraasi. Kerrotko hänelle vitsin piristääksesi häntä?\nA = Kyllä\nB = Ei")
        while True:
            if joke == "A":
                print("Pormestari hymyää hiljaa ja saat vahvistuksen, että hän jaksaa matkata kanssasi loppuun saakka.")
                mayorpoints += 3
                break
            elif joke == "B":
                print(f"Pormestari näyttää päättäväiseltä. Hän mulkaisee sinua viimeisen kerran ja juoksee karkuun.\nOlet päässyt velvollisuuksistasi, ja ainoa mitä sinulle jäi käteen (reppuun) on:\n{player1.itemlist}")
                player1.move(room6a)
    else:
        print("Kävelette päättäväisesti tietä pitkin kohti seuraavaa haastetta.\nPormestarin pienillä sardiinin kasvoilla näkyy vaihdellen huolta ja toivoa.")
        player1.move(room5)
        room5fun()

def room5fun():
    #roommove = {"A": room6bfun, "B": room6afun}
    print(f"Tämäpä erikoista! Saavutte paikkaan {player1.currentroom}.\nSuuren pesän ovella näkyy Pormestarille tuttu hahmo.\nPORMESTARI: 'Mauri! Pieni rakkaani! Missä olet ollut?'")
    print("Kuitenkin nopeasti huomaatte, ettei Mauri ole pieni lainkaan.\nTämä katkarapu on syönyt reilun määrän eikä mahtuisi enää edes kaupungintalon ovesta sisään.\nMauri näkyy myös silmäilevän sinua ja Pormestaria nälkäisesti.")
    if sanakirja in player1.inventory:
        usesanakirja = input("Mutta sinullahan on mukanasi Sardiini - Katkarapu -sanakirja! Käytätkö sitä Maurille jutteluun?\nA = Kyllä\nB = Ei")
        while True:
            if usesanakirja == "A":
                print("Maurin katseeseen tulee nälän sijaan tunnistus ja kaipuu.\nSanakirjan avulla puhuminen on humanisoinut teidät Maurin silmissä.\nMauri suostuu lähtemään Pormestarin mukana kotiin, vaikka hänen täytyykin nyt koostaan johtuen asua pihalla.")
                player1.move(room6b)
                break
            elif usesanakirja == "B":
                print("Mauri nähtävästi syö Pormestarin.\nEt toki ole aivan varma, koska olet jo lähtenyt juoksemaan kauas pois.")
                player1.move(room6a)
                
                break
            else:
                usesanakirja = input("Valitse A tai B....")
    elif pesis in player1.inventory:
        usepesis = input("Mutta hätä ei ole tämän näköinen, sinulla on pesäpallomaila mukanasi!\nKäytätkö sitä puolustamaan Pormestaria ja itseäsi nälkäiseltä Maurilta?\nA = Kyllä\nB = Ei")
        while True:
            if usepesis == "A":
                print("Mauri on nyt mäskinä, eikä päässyt syömään teitä.\nPormestari näyttää nyt hyvin hyvin surulliselta Maurin kohtalosta.\nLähdette sanattomina eri suuntiin.")
                player1.move(room6a)
                break
            elif usepesis == "B":
                print("Mauri nähtävästi syö Pormestarin.\nEt toki ole aivan varma, koska olet jo lähtenyt juoksemaan kauas pois.")
                player1.move(room6a)
                break
            else:
                usepesis = input("A tai B!!!")
    elif avain in player1.inventory:
        print("Vedät repustasi avaimen. Maurin katse kiinnittyy siihen.\nMAURI: 'blub blub blub???'\nMauri osoittaa oveensa ja tajuat avaimen olevan Maurin uuden kotipesän avain.")
        print("PORMESTARI: 'Mauri! Sinähän jätit minulle avaimesi vinkiksi!'\nMauri näyttää tunnistaneen Pormestarin, ja on halukas lähtemään mukananne kaupungintalolle.")
        player1.move(room6b)

def room6afun():
    print(f"Paikan nimi on {room6a.name}.\nOlet epäonnistunut tehtävässäsi, ja pettänyt Pormestarin.")

def room6bfun():
    print("Onnittelut!\nMauri on saatettu kotiin.\nPormestari on heti alkanut laajentamaan kaupungintalon ovea Maurille sopivaksi.")
    if mayorpoints >= 5:
        print("PORMESTARI: 'Kiitos sinulle kaikesta. Olet mahtava tyyppi.")
    elif mayorpoints <= 0:
        print("PORMESTARI: 'Kiitos...'")
    else:
        print("PORMESTARI: 'Kiitos vain!'")
    print("Lähdet tyytyväisin mielin kotiin.")



# greeting()
meetthemayor()
mainmenu()