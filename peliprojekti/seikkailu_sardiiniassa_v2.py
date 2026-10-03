import random

#Tarvitaan kaikille optioille: errorviestin (tyhjä kenttä) proofing, 
# tallennustoiminto, toiminto jotta voi komennolla tsekkaa mayorpoints
class Player:
    def __init__(self, name, age, currentroom, mayorpoints = 0):
        self.name = name
        self.age = age
        self.inventory = []
        self.currentroom = currentroom
        self.mayorpoints = mayorpoints
        
    def move(self, room):
        self.currentroom = room.name
    def collectitem(self, item):
        self.inventory.append(item)
        print(f"Reppuun lisättiin: {item.name}\n")
    def loseitem(self, item):
        self.inventory.remove(item)
        print(f"Repusta lähti: {item.name}\n")
    def itemlist(self):
        for i in self.inventory:
            print("Repussa on nyt:")
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
room3b1 = Room("Sardiinitehdas")
room3b2 = Room("Tehtaan konsolihuone")
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
kivi = Item("Kivi")

while True:
    if playerage < 12:
        print("Annoitko ikäsi vahingossa planktonvuosissa vai oletko vain noin nuori??? Tänne ei pieniä lapsia haluta!")
        playerage = int(input("Mikä on ikäsi?\n"))
    else:
        player1 = Player(playername, playerage, room1.name)
        print(f"Hei {playername}, {playerage}v. Tervetuloa Sardiiniaan!\nOlet nyt muikku, ja paikassa {player1.currentroom}.\n")
        break

def meetthemayor():
    print("Sardiinian pormestari tervehtii sinua.\nPORMESTARI: 'Hauska tavata. Olen hukannut lemmikkikatkarapuni Maurin, ja tarvitsen apua sen löytämiseen.\nOlisitko sinä tullut etsimään kanssani?'")
    hellomayor = input("A = Tervehdi pormestaria kuin normaali muikku ja lupaa auttavasi parhaan mukaan\nB = Sylkäise maahan ja nyökkää pormestarille\nC = Kumarra syvään ja sano 'Oi rouva pormestari; vannon sinulle uskollisuuteni'\n")
    def maya():
        player1.mayorpoints += random.randint(2,4)
        return "Pormestari kiittää sinua. Voit erottaa hänen silmäkulmastaan helpotuksen kyyneleen.\n"
    def mayb():
        player1.mayorpoints += 1
        return "Pormestari vilkaisee sinua kauhuissaan, mutta hyväksyy vastauksen hiljaa nyökäten. Kaikki apu on tarpeen.\n"
    def mayc():
        player1.mayorpoints -= 1
        return "Pormestaria näkyvästi etoo limainen käytöksesi.\nPORMESTARI: 'Olet melko erikoinen, mutta apusi on silti tarpeen...'\n"
    while hellomayor != "A" and hellomayor != "B" and hellomayor != "C":
        hellomayor = input("Anna vastaus A, B tai C.\n")
    choices = {"A": maya, "B": mayb, "C": mayc}
    room_fun = choices.get(hellomayor)
    print(room_fun())


def mainmenu():
    print("PORMESTARI: 'Voit valita yhden tavaran mukaan kaupungintalon vitriinistä. Toivon mukaan siitä on meille apua.'\n")
    firstitem = input("Valitse hyllyltä yksi (1) esine:\nA = Sardiini - Katkarapu -sanakirja\nB = Pesäpallomaila (muikulle sopivan kokoinen)\nC = Avain\n")
    if firstitem == "A":
        player1.collectitem(sanakirja)
    elif firstitem == "B":
        player1.collectitem(pesis)
    elif firstitem == "C":
        player1.collectitem(avain)
    else:
        print("Tuo ei ollu A, B, tai C. Et saa mitään.")
    print("Hyvä. Pääsette aloittamaan matkanne. Tie erkanee kahteen suuntaan.\nTie A näkyy johtavan... kohti juottolaa? Tie B taas vie jonkun kotipihaan.")
    crossing()

def crossing():
    crossing1 = input("Haluatko tien A vai B?\n")
    while crossing1 != "A" and crossing1 != "B":
        crossing1 = input("Niin siis A vai B?\n")
    if crossing1 == "A":
        player1.move(room2a)
        room2afun()
    elif crossing1 == "B":
        player1.move(room2b)
        room2bfun()
        

def room2afun():
    print(f"Saavutte paikkaan {player1.currentroom}. Pormestari kavahtaa paikan hajua.\nPaikan kanta-asiakas nappaa tiskiltä rätin ja heittää sinua sillä. Saat kopin.\nBaarimikko nauraa räkäisesti tapahtuneelle.")
    player1.collectitem(ratti)
    print("BAARIMIKKO: 'Tervetuloa Sihisevään Sardiiniin. Haluatteko juotavaa?'\nPORMESTARI: 'Ei missään nimessä. Etsimme kadonnutta katkarapuani Mauria. Onko täällä näkynyt?'")
    print("BAARIMIKKO: 'En ehdi katselemaan sellaisia työn ohella, mutta voitte itse tutkia pubini paikat jos haluatte.'")
    crossing2a = input("Pormestari vilkaisee ensin Baarimikkoa epäilevästi, ja sitten osoittaa kahta ovea baarin takaseinustalla.\nOtatko oven A vai B?\n")
    while crossing2a != "A" and crossing2a != "B":
        crossing2a = input("Tuo ei ole A tai B. Valitse A tai B\n")
    if crossing2a == "A":
        player1.move(room3a1)
        room3a1fun()
    elif crossing2a == "B":
        player1.move(room3a2)
        room3a2fun()
    else:
        crossing2a = input("Tuo ei ole A tai B. Valitse A tai B")

def room2bfun():
    print(f"Saavutte paikkaan {room2b}. Seppo Sardiini istuu kuistillaan siemaillen tomaattimehua.\nSEPPO: 'Kuka siellä kulkee?'")
    seppomeet = input("Mitä kerrot Sepolle tilanteesta?\nA = Selitä kuinka jalosti autat kyvytöntä Pormestaria etsimään lemmikkiään Mauria\nB = Kerro kuinka Mauri on karannut kotoaan, ja etsitte häntä yhdessä Pormestarin kanssa\nC = Kysy Sepolta mikä oikeuttaa hänet kysymään\n")
    while seppomeet != "A" and seppomeet != "B" and seppomeet != "C":
        seppomeet = input("A, B vai C?\n")
    if seppomeet == "A":
        player1.mayorpoints -= 2
        print("Seppo Sardiini hymähtää.\nSEPPO: 'Olenhan saattanut nähdä tuon otuksen... Ja tunnen katkaravut hyvin.'\nPormestari mulkaisee sinua sanavalintojesi johdosta, mutta viittoo silti Seppoa jatkamaan.\n")
        print("SEPPO: 'Jos vain kuljette suoraan takapihani läpi, pääsette Sardiinitehtaan alueelle. Alue on aidattu ja vaarallinen, mutta sinne Mauri suuntasi...'")
        print("Suuntaatte heti Sepon takapihalle, ja siitä kohti tehdasta.")
        room3b1fun()
    elif seppomeet == "B":
        player1.mayorpoints +=1
        print("SEPPO: 'Vai niin on käynyt! Minähän näin Maurin ryömimässä kohti Sardiinitehdasta toissapäivänä.\nPormestarin silmiin tulee toivon häivä.")
        print("SEPPO: 'Kyllä näin on näreet.. Ottakaa kuitenkin tästä juotavaa matkalle vielä.'\nSeppo ojentaa sinulle pullon jossa on... nestettä? Ehkä se on juotavaa.\nSuuntaatte Sepon takapihalle ja siitä kohti tehdasta.")
        room3b1fun()
    elif seppomeet == "C":
        player1.mayorpoints -= 3
        print("SEPPO: 'Pormestari, tällaistako seuraa sinä pidät?'\nPormestari näyttää nolostuneelta.")
        seppochoice = input("Pyydätkö Sepolta anteeksi? Se voi auttaa teitä eteenpäin matkallanne.\nA = Kyllä\nB = Ei")
        while seppochoice != "A" and seppochoice != "B":
            seppochoice = input("A tai B!!! Ei mitään muuta.")
        if seppochoice == "A":
            player1.move(room3b1)
            room3b1fun()
        elif seppochoice == "B":
            player1.move(room6a)
            room6afun()
    

def room3b1fun():
    print(f"Saavutte paikkaan {player1.currentroom}.\nTehtaan ovi pamahtaa kiinni takananne.\nPormestari säpsähtää, ja hikikarpalo valuu otsaltasi.\n")
    creaturechoice = input("Tehtaan pimeästä nurkasta pötkähtää ulos merimakkara.\nSen ilmeitä on vaikea lukea koska sillä ei ole kasvoja, mutta tunnet siitä huokuvan pahuuden.\nEhkä sinun täytyy iskeä ensin...\nMitä teet?\nA = Juokse kuin pelkuri\nB = Suojaa Pormestaria\n")
    while creaturechoice != "A" and creaturechoice != "B":
        creaturechoice = input("Anna vastaukseksi A tai B.")
    def fight():
        if sanakirja in player1.inventory:
            sfight = input("Sinulla näkyy olevan taskussasi sanakirja.\nSiitä ei ole hyötyä taistelussa. Vai onko?\nValitse:\nA = Heitä pahaa merimakkaraa sanakirjalla\nB = Anna sanakirjan pysyä repussasi\n")
            while sfight != "A" and sfight != "B":
                sfight = input("A vai B?")
            if sfight == "A":
                luck = random.randint(1,11)
                if luck >= 5:
                    print("Kirja osuu makkaraan! Pormestari on vaikuttunut. Pääsette juoksemaan kohti tehtaan takaovea.\nPormestari potkaisee oven auki, ja juoksette henkenne edestä kohti...\nOnko tuo jonkun pesä?\n")
                    player1.mayorpoints += 4
                    player1.move(room5)
                    room5fun()
                else:
                    print("Kirjan lento jää lyhyeksi, mutta makkara näkyy kiinnostuneen siitä hieman enemmän kuin teistä.\nHiippailette hiljaa kohti tehtaan takaovea kun merimakkara lukee sanakirjaa.\nPormestari näkyy hieman pettyneen heittotaitoihisi.\n")
                    player1.mayorpoints -= 1
                    player1.move(room5)
                    room5fun()
        elif pesis in player1.inventory:
            print("Sinullahan on repussasi pesäpallomaila!\nHeilautat mailaa merimakkaraa päin. Makkara vingahtaa pelosta, ja vaikka et näe sillä kasvonpiirteitä, se ilmeisesti sulkee silmänsä.\nPääsette juoksemaan ulos tehtaan takaovesta.\nErotat kauempaa rakennelman, joka vaikuttaa jonkun pesältä, ja Pormestari pinkoo suoraan sitä kohti.\n")
            player1.move(room5)
            room5fun()
        else:
            print("Mitä tässä oikein voi tehdä? Sinulla ei ole mitään hyödyllistä mukanasi.\nTehtaan takaovi näkyy merimakkaran takana, mutta miten sinne pääsisi?\nLevittelet eviäsi Pormestarille, mutta hän on jo lähtenyt pinkomaan kohti merimakkaraa.\nMakkara kirkuu peloissaan.")
            print("Pormestari lyö makkaraa pyrstöllään. Makkara taintuu hetkeksi, ja ehditte juosta tehtaan takaovesta ulos.")
            player1.move(room5)
            room5fun()
    def flight():
        player1.mayorpoints -= 2
        print("Juokset kohti lähintä ovea. Pormestari tuhahtaa pelkuruutesi vuoksi, mutta seuraa nopeasti mukana.")
        player1.move(room3b2)
        room3b2fun()
    choices = {"A": flight, "B": fight}
    room_fun = choices.get(creaturechoice)
    room_fun()

def room3b2fun():
    rock = input(f"Saavutte paikkaan {player1.currentroom}.\nHuoneessa ei näy olevan takaovea.\nHuomaat kuitenkin lattialla pienen kiven.\nOtatko kiven mukaasi?\nA = Kyllä\nB = Ei\n")
    while rock != "A" and rock != "B":
        rock = input("A vai B?\n")
    if rock == "A":
        player1.collectitem("Kivi")
    player1.move(room3b1)
    room3b1fun()

def room3b1bfun():
    print("Täällä taas.\nMakkara näyttää verenhimoiselta. Sen takana erotat tehtaan takaoven.\n")
    if kivi in player1.inventory:
        print("Mutta sinullahan on kivi mukanasi!\nHeität merimakkaraa päin..")
        throw = random.randint(1,11)
        if throw >= 5:
            player1.mayorpoints += 1
            print("Ja se osuu! Makkara taintuu ja juoksette kovaa vauhtia ulos tehtaan takaovesta.\n")
            player1.move(room5)
            room5fun()
        else:
            print("Kivi lentää aivan liian kauas makkarasta.\nMutta kimpoaa seinästä ja osuu makkaran toiseen päätyyn (vaikea sanoa koska sillä ei varsinaisesti ole kasvoja).\nSen pyöriessä hämmentyneenä pääsette juoksemaan kohti tehtaan takaovea.\n")
            player1.mayorpoints += 3
            player1.move(room5)
            room5fun()
    else:
        if sanakirja in player1.inventory:
            sfight = input("Sinulla näkyy olevan taskussasi sanakirja.\nSiitä ei ole hyötyä taistelussa. Vai onko?\nValitse:\nA = Heitä pahaa merimakkaraa sanakirjalla\nB = Anna sanakirjan pysyä repussasi\n")
            while sfight != "A" and sfight != "B":
                sfight = input("A vai B?")
            if sfight == "A":
                luck = random.randint(1,11)
                if luck >= 5:
                    print("Kirja osuu makkaraan! Pormestari on vaikuttunut. Pääsette juoksemaan kohti tehtaan takaovea.\nPormestari potkaisee oven auki, ja juoksette henkenne edestä kohti...\nOnko tuo jonkun pesä?\n")
                    player1.mayorpoints += 4
                    player1.move(room5)
                    room5fun()
                else:
                    print("Kirjan lento jää lyhyeksi, mutta makkara näkyy kiinnostuneen siitä hieman enemmän kuin teistä.\nHiippailette hiljaa kohti tehtaan takaovea kun merimakkara lukee sanakirjaa.\nPormestari näkyy hieman pettyneen heittotaitoihisi.\n")
                    player1.mayorpoints -= 1
                    player1.move(room5)
                    room5fun()
        elif pesis in player1.inventory:
            print("Sinullahan on repussasi pesäpallomaila!\nHeilautat mailaa merimakkaraa päin. Makkara vingahtaa pelosta, ja vaikka et näe sillä kasvonpiirteitä, se ilmeisesti sulkee silmänsä.\nPääsette juoksemaan ulos tehtaan takaovesta.\nErotat kauempaa rakennelman, joka vaikuttaa jonkun pesältä, ja Pormestari pinkoo suoraan sitä kohti.\n")
            player1.move(room5)
            room5fun()
        else:
            print("Mitä tässä oikein voi tehdä? Sinulla ei ole mitään hyödyllistä mukanasi.\nTehtaan takaovi näkyy merimakkaran takana, mutta miten sinne pääsisi?\nLevittelet eviäsi Pormestarille, mutta hän on jo lähtenyt pinkomaan kohti merimakkaraa.\nMakkara kirkuu peloissaan.")
            print("Pormestari lyö makkaraa pyrstöllään. Makkara taintuu hetkeksi, ja ehditte juosta tehtaan takaovesta ulos.")
            player1.move(room5)
            room5fun()

def room3a1fun():
    print(f"Saavutte paikkaan {player1.currentroom}.\nHuone näyttää pölyiseltä, mutta muuten siistiltä.")
    useitemratti = input("Mauria ei näy huoneessa, mutta sinulla on tilaisuus tehdä hyvä teko ja pyyhkiä rätillä pölyjä pois.\nKäytätkö rättiä?\nA = Kyllä\nB = Ei\n")
    while useitemratti != "A" and useitemratti != "B":
        useitemratti = input("Valitse A tai B.\n")
    if useitemratti == "A":
        player1.inventory.remove(ratti)
        player1.mayorpoints += 4
        print("PORMESTARI: 'Olipa mukavasti tehty.\n")
    elif useitemratti == "B":
        player1.mayorpoints -= 1
            
    print("Aika lähteä, Mauri ei ole täällä. Huoneessa on takaovi, josta Pormestari jo sujahtaa ulos.\n")
    player1.move(room4a)
    room4afun()

def room3a2fun():
    print(f"Saavutte paikkaan {player1.currentroom}. Mauria ei näy, mutta nurkassa kyhjöttää pieni surkea sardiini lian peitossa.\nNURKKASARDIINI: 'Tulitteko tekin pilkkaamaan minua? Nuoret sardiinit heittivät päälleni jotain tuosta lattialta enkä uskalla poistua...'\n")
    useitemratti2 = input("Pormestarilla on tippa silmäkulmassa. Liikuttaako sinuakin Nurkkasardiinin huono kohtelu?\nKäytätkö rättiä hänen putsaamiseensa?\nA = Kyllä\nB = Ei\n")
    while useitemratti2 != "A" and useitemratti2 != "B":
        useitemratti2 = ("Valitse A tai B!\n")
    if useitemratti2 == "A":
        player1.loseitem(ratti)
        player1.mayorpoints += 5
        print("NURKKASARDIINI: 'Kiitos! Kiitos tuhannesti!'\n")
    elif useitemratti2 == "B":
        player1.mayorpoints -= 2
        ("Oletpas pihi kun et rättiä viitsi käyttää!\n")

    print("Aika lähteä, Mauri ei ole täällä. Pormestari ryömii jo ulos vessan ikkunasta kohti levämetsää.\n")
    player1.move(room4b)
    room4bfun()
    

def room4afun():
    print(f"Saavutte paikkaan {player1.currentroom}. Edessä aukeaa tie, joka johtaa vain yhteen suuntaan.\n")
    if player1.mayorpoints >= 0:
        joke = input("Pormestari vaikuttaa jo kyllästyneen seuraasi. Kerrotko hänelle vitsin piristääksesi häntä?\nA = Kyllä\nB = Ei\n")
        while joke != "A" and joke != "B":
            joke = input("A vai B?")
        if joke == "A":
            print("Pormestari hymyää hiljaa ja saat vahvistuksen, että hän jaksaa matkata kanssasi loppuun saakka.\n")
            player1.mayorpoints += 3
            player1.move(room5)
            room5fun()
        elif joke == "B":
            print(f"Pormestari näyttää päättäväiseltä. Hän mulkaisee sinua viimeisen kerran ja juoksee karkuun.\nOlet päässyt velvollisuuksistasi, ja ainoa mitä sinulle jäi käteen (reppuun) on:\n{player1.itemlist}")
            player1.move(room6a)
            room6afun()
    else:
        print("Kävelette päättäväisesti tietä pitkin kohti seuraavaa haastetta.\nPormestarin pienillä sardiinin kasvoilla näkyy vaihdellen huolta ja toivoa.\n")
        player1.move(room5)
        room5fun()

def room4bfun():
    print(f"Saavutte paikkaan {player1.currentroom}.\nMetsä on pimeä, mutta näet kauempana metsässä valonsäteitä jotka antavat toivoa ettei metsä jatku loputtomiin.")
    forestchoice = input("Edessä on kuitenkin paljon matkaa, ja Pormestari vaikuttaa väsyneeltä.\nKannatko Pormestaria?\nA = Kyllä, olen herrasmuikku\nB = En, olen ilkeä\n")
    while forestchoice != "A" and forestchoice != "B":
        forestchoice = input("A vai B...")
    if forestchoice == "A":
        player1.mayorpoints += 4
        print("PORMESTARI: 'Oi kiitos! En toki ole kovin vanha, mutta olen laiska kulkemaan pitkiä matkoja...'\n")
    elif forestchoice == "B":
        print("Ok, laiskuri..\n")
    print("Metsän loppu häämöttää jo, ja pääsette vihdoin tielle joka näkyy johtavan kohti jonkinlaista rakennelmaa.\n")
    player1.move(room5)
    room5fun()

def room5fun():
    #roommove = {"A": room6bfun, "B": room6afun}
    print(f"Tämäpä erikoista! Saavutte paikkaan {player1.currentroom}.\nSuuren pesän ovella näkyy Pormestarille tuttu hahmo.\nPORMESTARI: 'Mauri! Pieni rakkaani! Missä olet ollut?'\n")
    print("Kuitenkin nopeasti huomaatte, ettei Mauri ole pieni lainkaan.\nTämä katkarapu on syönyt reilun määrän eikä mahtuisi enää edes kaupungintalon ovesta sisään.\nMauri näkyy myös silmäilevän sinua ja Pormestaria nälkäisesti.\n")
    if sanakirja in player1.inventory:
        usesanakirja = input("Mutta sinullahan on mukanasi Sardiini - Katkarapu -sanakirja! Käytätkö sitä Maurille jutteluun?\nA = Kyllä\nB = Ei\n")
        while usesanakirja != "A" and usesanakirja != "B":
            usesanakirja = input("Valitse A tai B....\n")

        if usesanakirja == "A":
            print("Maurin katseeseen tulee nälän sijaan tunnistus ja kaipuu.\nSanakirjan avulla puhuminen on humanisoinut teidät Maurin silmissä.\nMauri suostuu lähtemään Pormestarin mukana kotiin, vaikka hänen täytyykin nyt koostaan johtuen asua pihalla.\n")
            player1.move(room6b)
            room6bfun()
        
        elif usesanakirja == "B":
            print("Mauri nähtävästi syö Pormestarin.\nEt toki ole aivan varma, koska olet jo lähtenyt juoksemaan kauas pois.\n")
            player1.move(room6a)
            room6afun()
            
    elif pesis in player1.inventory:
        usepesis = input("Mutta hätä ei ole tämän näköinen, sinulla on pesäpallomaila mukanasi!\nKäytätkö sitä puolustamaan Pormestaria ja itseäsi nälkäiseltä Maurilta?\nA = Kyllä\nB = Ei\n")
        while usepesis != "A" and usepesis != "B":
            usepesis = input("A tai B!!!")
        if usepesis == "A":
            print("Mauri on nyt mäskinä, eikä päässyt syömään teitä.\nPormestari näyttää nyt hyvin hyvin surulliselta Maurin kohtalosta.\nLähdette sanattomina eri suuntiin.\n")
            player1.move(room6a)
            room6afun()
            
        elif usepesis == "B":
            print("Mauri nähtävästi syö Pormestarin.\nEt toki ole aivan varma, koska olet jo lähtenyt juoksemaan kauas pois.\n")
            player1.move(room6a)
            room6afun()
            
    elif avain in player1.inventory:
        print("Vedät repustasi avaimen. Maurin katse kiinnittyy siihen.\nMAURI: 'blub blub blub???'\nMauri osoittaa oveensa ja tajuat avaimen olevan Maurin uuden kotipesän avain.\n")
        print("PORMESTARI: 'Mauri! Sinähän jätit minulle avaimesi vinkiksi!'\nMauri näyttää tunnistaneen Pormestarin, ja on halukas lähtemään mukananne kaupungintalolle.\n")
        player1.move(room6b)
        room6bfun()

def room6afun():
    print(f"Paikan nimi on {room6a.name}.\nOlet epäonnistunut tehtävässäsi, ja pettänyt Pormestarin.\n\033[1;31mGAME OVER\033[0m")

def room6bfun():
    print("Onnittelut!\nMauri on saatettu kotiin.\nPormestari on heti alkanut laajentamaan kaupungintalon ovea Maurille sopivaksi.")
    if mayorpoints >= 7:
        print("PORMESTARI: 'Kiitos sinulle kaikesta. Olet mahtava tyyppi.\n")
    elif mayorpoints <= 0:
        print("PORMESTARI: 'Kiitos...'\n")
    else:
        print("PORMESTARI: 'Kiitos vain!'\n")
    print("Hyviä tekoja on tehty tänään.\nLähdet tyytyväisin mielin kotiin.\n♡(◔ω◔ )♡")



# greeting()
meetthemayor()
mainmenu()