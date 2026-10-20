import random
from items import items_dict

class Room:
    def __init__(self, name, room_func, item=None):
        self.name = name
        self.item = item
        self.room_func = room_func
    def play_room(self, player):
        return self.room_func(player)


def meetthemayor(player_in_room):
    print("Sardiinian pormestari tervehtii sinua.\nPORMESTARI: 'Hauska tavata. Olen hukannut lemmikkikatkarapuni Maurin, ja tarvitsen apua sen löytämiseen.\nOlisitko sinä tullut etsimään kanssani?'")
    hellomayor = input("A = Tervehdi pormestaria kuin normaali muikku ja lupaa auttavasi parhaan mukaan\nB = Sylkäise maahan ja nyökkää pormestarille\nC = Kumarra syvään ja sano 'Oi rouva pormestari; vannon sinulle uskollisuuteni'\n")
    def maya():
        player_in_room.mayorpoints += random.randint(2,4)
        return "Pormestari kiittää sinua. Voit erottaa hänen silmäkulmastaan helpotuksen kyyneleen.\n"
    def mayb():
        player_in_room.mayorpoints += 1
        return "Pormestari vilkaisee sinua kauhuissaan, mutta hyväksyy vastauksen hiljaa nyökäten. Kaikki apu on tarpeen.\n"
    def mayc():
        player_in_room.mayorpoints -= 1
        return "Pormestaria näkyvästi etoo limainen käytöksesi.\nPORMESTARI: 'Olet melko erikoinen, mutta apusi on silti tarpeen...'\n"
    while hellomayor != "A" and hellomayor != "B" and hellomayor != "C":
        hellomayor = input("Anna vastaus A, B tai C.\n")
    choices = {"A": maya, "B": mayb, "C": mayc}
    room_fun = choices.get(hellomayor)
    print(room_fun())


def mainmenu(player_in_room):
    print("PORMESTARI: 'Voit valita yhden tavaran mukaan kaupungintalon vitriinistä. Toivon mukaan siitä on meille apua.'\n")
    firstitem = input("Valitse hyllyltä yksi (1) esine:\nA = Sardiini - Katkarapu -sanakirja\nB = Pesäpallomaila (muikulle sopivan kokoinen)\nC = Avain\n")
    if firstitem == "A":
        player_in_room.collectitem(items_dict.get("sanakirja"))
    elif firstitem == "B":
        player_in_room.collectitem(items_dict.get("pesis"))
    elif firstitem == "C":
        player_in_room.collectitem(items_dict.get("avain"))
    else:
        print("Tuo ei ollu A, B, tai C. Et saa mitään.\n")
    print("Hyvä. Pääsette aloittamaan matkanne. Tie erkanee kahteen suuntaan.\nTie A näkyy johtavan... kohti juottolaa? Tie B taas vie jonkun kotipihaan.")
    nextroom = "crossing"
    player_in_room.move(rooms_dict.get(nextroom))
    return nextroom

def crossing(player_in_room):
    crossing1 = input("Haluatko tien A vai B?\n")
    while crossing1 != "A" and crossing1 != "B":
        crossing1 = input("Niin siis A vai B?\n")
    if crossing1 == "A":
        nextroom = "room2a"
        player_in_room.move(rooms_dict.get(nextroom))
        return nextroom
    if crossing1 == "B":
        nextroom = "room2b"
        player_in_room.move(rooms_dict.get(nextroom))
        return nextroom
    
        

def room2afun(player_in_room):
    print(f"Saavutte paikkaan {player_in_room.current_room.name}. Pormestari kavahtaa paikan hajua.\nPaikan kanta-asiakas nappaa tiskiltä rätin ja heittää sinua sillä. Saat kopin.\nBaarimikko nauraa räkäisesti tapahtuneelle.")
    player_in_room.collectitem(items_dict.get("ratti"))
    print("BAARIMIKKO: 'Tervetuloa Sihisevään Sardiiniin. Haluatteko juotavaa?'\nPORMESTARI: 'Ei missään nimessä. Etsimme kadonnutta katkarapuani Mauria. Onko täällä näkynyt?'")
    print("BAARIMIKKO: 'En ehdi katselemaan sellaisia työn ohella, mutta voitte itse tutkia pubini paikat jos haluatte.'")
    crossing2a = input("Pormestari vilkaisee ensin Baarimikkoa epäilevästi, ja sitten osoittaa kahta ovea baarin takaseinustalla.\nOtatko oven A vai B?\n")
    while crossing2a != "A" and crossing2a != "B":
        crossing2a = input("Tuo ei ole A tai B. Valitse A tai B\n")
    if crossing2a == "A":
        nextroom = "room3a1"
        player_in_room.move(rooms_dict.get(nextroom))
        return nextroom
    elif crossing2a == "B":
        nextroom = "room3a2"
        player_in_room.move(rooms_dict.get(nextroom))
        return nextroom


def room2bfun(player_in_room):
    print(f"Saavutte paikkaan {player_in_room.current_room.name}. Seppo Sardiini istuu kuistillaan siemaillen tomaattimehua.\nSEPPO: 'Kuka siellä kulkee?'")
    seppomeet = input("Mitä kerrot Sepolle tilanteesta?\nA = Selitä kuinka jalosti autat kyvytöntä Pormestaria etsimään lemmikkiään Mauria\nB = Kerro kuinka Mauri on karannut kotoaan, ja etsitte häntä yhdessä Pormestarin kanssa\nC = Kysy Sepolta mikä oikeuttaa hänet kysymään\n")
    while seppomeet != "A" and seppomeet != "B" and seppomeet != "C":
        seppomeet = input("A, B vai C?\n")
    if seppomeet == "A":
        player_in_room.mayorpoints -= 2
        print("Seppo Sardiini hymähtää.\nSEPPO: 'Olenhan saattanut nähdä tuon otuksen... Ja tunnen katkaravut hyvin.'\nPormestari mulkaisee sinua sanavalintojesi johdosta, mutta viittoo silti Seppoa jatkamaan.\n")
        print("SEPPO: 'Jos vain kuljette suoraan takapihani läpi, pääsette Sardiinitehtaan alueelle. Alue on aidattu ja vaarallinen, mutta sinne Mauri suuntasi...'")
        print("Suuntaatte heti Sepon takapihalle, ja siitä kohti tehdasta.\n")
        nextroom = "room3b1"
        player_in_room.move(rooms_dict.get(nextroom))
        return nextroom
    elif seppomeet == "B":
        player_in_room.mayorpoints +=1
        print("SEPPO: 'Vai niin on käynyt! Minähän näin Maurin ryömimässä kohti Sardiinitehdasta toissapäivänä.\nPormestarin silmiin tulee toivon häivä.")
        print("SEPPO: 'Kyllä näin on näreet.. Ottakaa kuitenkin tästä juotavaa matkalle vielä.'\nSeppo ojentaa sinulle pullon jossa on... nestettä? Ehkä se on juotavaa.\nSuuntaatte Sepon takapihalle ja siitä kohti tehdasta.\n")
        player_in_room.collectitem(items_dict.get("juoma"))
        nextroom = "room3b1"
        player_in_room.move(rooms_dict.get(nextroom))
        return nextroom
    elif seppomeet == "C":
        player_in_room.mayorpoints -= 3
        print("SEPPO: 'Pormestari, tällaistako seuraa sinä pidät?'\nPormestari näyttää nolostuneelta.\n")
        seppochoice = input("Pyydätkö Sepolta anteeksi? Se voi auttaa teitä eteenpäin matkallanne.\nA = Kyllä\nB = Ei\n")
        while seppochoice != "A" and seppochoice != "B":
            seppochoice = input("A tai B!!! Ei mitään muuta.\n")
        if seppochoice == "A":
            nextroom = "room3b1"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom
        elif seppochoice == "B":
            nextroom = "room6a"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom
    

def room3b1fun(player_in_room):
    print(f"Saavutte paikkaan {player_in_room.current_room.name}.\nSardiineilla ei ole enää tarvetta tehtaalle, joten yhtään työntekijää ei ole näkyvissä.\nTehtaan ovi pamahtaa kiinni takananne.\nPormestari säpsähtää, ja hikikarpalo valuu otsaltasi.\n")
    creaturechoice = input("Tehtaan pimeästä nurkasta pötkähtää ulos merimakkara (vieraslaji alueella).\nSen ilmeitä on vaikea lukea koska sillä ei ole kasvoja, mutta tunnet siitä huokuvan pahuuden.\nEhkä sinun täytyy iskeä ensin...\nMitä teet?\nA = Juokse kuin pelkuri\nB = Suojaa Pormestaria\n")
    while creaturechoice != "A" and creaturechoice != "B":
        creaturechoice = input("Anna vastaukseksi A tai B.\n")
    def fight():
        if items_dict.get("sanakirja") in player_in_room.inventory:
            sfight = input("Sinulla näkyy olevan taskussasi sanakirja.\nSiitä ei ole hyötyä taistelussa. Vai onko?\nValitse:\nA = Heitä pahaa merimakkaraa sanakirjalla\nB = Anna sanakirjan pysyä repussasi\n")
            while sfight != "A" and sfight != "B":
                sfight = input("A vai B?")
            if sfight == "A":
                luck = random.randint(1,11)
                if luck >= 5:
                    print("Kirja osuu makkaraan! Pormestari on vaikuttunut. Pääsette juoksemaan kohti tehtaan takaovea.\nPormestari potkaisee oven auki, ja juoksette henkenne edestä kohti...\nOnko tuo jonkun pesä?\n")
                    player_in_room.mayorpoints += 4
                    player_in_room.loseitem(items_dict.get("sanakirja"))
                    nextroom = "room5"
                    player_in_room.move(rooms_dict.get(nextroom))
                    return nextroom
                else:
                    print("Kirjan lento jää lyhyeksi, mutta makkara näkyy kiinnostuneen siitä hieman enemmän kuin teistä.\nHiippailette hiljaa kohti tehtaan takaovea kun merimakkara lukee sanakirjaa.\nPormestari näkyy hieman pettyneen heittotaitoihisi.\n")
                    player_in_room.mayorpoints -= 1
                    player_in_room.loseitem(items_dict.get("sanakirja"))
                    nextroom = "room5"
                    player_in_room.move(rooms_dict.get(nextroom))
                    return nextroom
        elif items_dict.get("pesis") in player_in_room.inventory:
            print("Sinullahan on repussasi pesäpallomaila!\nHeilautat mailaa merimakkaraa päin. Makkara vingahtaa pelosta, ja vaikka et näe sillä kasvonpiirteitä, se ilmeisesti sulkee silmänsä.\nPääsette juoksemaan ulos tehtaan takaovesta.\nErotat kauempaa rakennelman, joka vaikuttaa jonkun pesältä, ja Pormestari pinkoo suoraan sitä kohti.\n")
            nextroom = "room5"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom
        else:
            print("Mitä tässä oikein voi tehdä? Sinulla ei ole mitään hyödyllistä mukanasi.\nTehtaan takaovi näkyy merimakkaran takana, mutta miten sinne pääsisi?\nLevittelet eviäsi Pormestarille, mutta hän on jo lähtenyt pinkomaan kohti merimakkaraa.\nMakkara kirkuu peloissaan.\n")
            print("Pormestari lyö makkaraa pyrstöllään.\nMakkara taintuu hetkeksi, ja ehditte juosta tehtaan takaovesta ulos.\n")
            nextroom = "room5"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom
    def flight():
        player_in_room.mayorpoints -= 2
        print("Juokset kohti lähintä ovea. Pormestari tuhahtaa pelkuruutesi vuoksi, mutta seuraa nopeasti mukana.\n")
        nextroom = "room3b2"
        player_in_room.move(rooms_dict.get(nextroom))
        return nextroom
    choices = {"A": flight, "B": fight}
    room_fun = choices.get(creaturechoice)
    return room_fun()

def room3b2fun(player_in_room):
    rock = input(f"Saavutte paikkaan {player_in_room.current_room.name}.\nHuoneessa ei näy olevan takaovea.\nHuomaat kuitenkin lattialla pienen kiven.\nOtatko kiven mukaasi?\nA = Kyllä\nB = Ei\n")
    while rock != "A" and rock != "B":
        rock = input("A vai B?\n")
    if rock == "A":
        player_in_room.collectitem(items_dict.get("kivi"))
    nextroom = "room3b1b"
    player_in_room.move(rooms_dict.get(nextroom))
    return nextroom

def room3b1bfun(player_in_room):
    print("Täällä taas.\nMakkara näyttää verenhimoiselta. Sen takana erotat tehtaan takaoven.\n")
    if items_dict.get("kivi") in player_in_room.inventory:
        print("Mutta sinullahan on kivi mukanasi!\nHeität merimakkaraa päin..")
        throw = random.randint(1,11)
        if throw >= 5:
            player_in_room.mayorpoints += 1
            player_in_room.loseitem(items_dict.get("kivi"))
            print("Ja se osuu! Makkara taintuu ja juoksette kovaa vauhtia ulos tehtaan takaovesta.\n")
            nextroom = "room5"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom
        else:
            print("Kivi lentää aivan liian kauas makkarasta.\nMutta kimpoaa seinästä ja osuu makkaran toiseen päätyyn (vaikea sanoa koska sillä ei varsinaisesti ole kasvoja).\nSen pyöriessä hämmentyneenä pääsette juoksemaan kohti tehtaan takaovea.\n")
            player_in_room.mayorpoints += 3
            nextroom = "room5"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom
    else:
        if items_dict.get("sanakirja") in player_in_room.inventory:
            sfight = input("Sinulla näkyy olevan taskussasi sanakirja.\nSiitä ei ole hyötyä taistelussa. Vai onko?\nValitse:\nA = Heitä pahaa merimakkaraa sanakirjalla\nB = Anna sanakirjan pysyä repussasi\n")
            while sfight != "A" and sfight != "B":
                sfight = input("A vai B?")
            if sfight == "A":
                luck = random.randint(1,11)
                if luck >= 5:
                    print("Kirja osuu makkaraan! Pormestari on vaikuttunut. Pääsette juoksemaan kohti tehtaan takaovea.\nPormestari potkaisee oven auki, ja juoksette henkenne edestä kohti...\nOnko tuo jonkun pesä?\n")
                    player_in_room.mayorpoints += 4
                    player_in_room.loseitem(items_dict.get("sanakirja"))
                    nextroom = "room5"
                    player_in_room.move(rooms_dict.get(nextroom))
                    return nextroom
                else:
                    print("Kirjan lento jää lyhyeksi, mutta makkara näkyy kiinnostuneen siitä hieman enemmän kuin teistä.\nHiippailette hiljaa kohti tehtaan takaovea kun merimakkara lukee sanakirjaa.\nPormestari näkyy hieman pettyneen heittotaitoihisi.\n")
                    player_in_room.mayorpoints -= 1
                    nextroom = "room5"
                    player_in_room.move(rooms_dict.get(nextroom))
                    return nextroom
        elif items_dict.get("pesis") in player_in_room.inventory:
            print("Sinullahan on repussasi pesäpallomaila!\nHeilautat mailaa merimakkaraa päin. Makkara vingahtaa pelosta, ja vaikka et näe sillä kasvonpiirteitä, se ilmeisesti sulkee silmänsä.\nPääsette juoksemaan ulos tehtaan takaovesta.\nErotat kauempaa rakennelman, joka vaikuttaa jonkun pesältä, ja Pormestari pinkoo suoraan sitä kohti.\n")
            nextroom = "room5"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom
        else:
            print("Mitä tässä oikein voi tehdä? Sinulla ei ole mitään hyödyllistä mukanasi.\nTehtaan takaovi näkyy merimakkaran takana, mutta miten sinne pääsisi?\nLevittelet eviäsi Pormestarille, mutta hän on jo lähtenyt pinkomaan kohti merimakkaraa.\nMakkara kirkuu peloissaan.\n")
            print("Pormestari lyö makkaraa pyrstöllään. Makkara taintuu hetkeksi, ja ehditte juosta tehtaan takaovesta ulos.\n")
            nextroom = "room5"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom

def room3a1fun(player_in_room):
    print(f"Saavutte paikkaan {player_in_room.current_room.name}.\nHuone näyttää pölyiseltä, mutta muuten siistiltä.\n")
    useitemratti = input("Mauria ei näy huoneessa, mutta sinulla on tilaisuus tehdä hyvä teko ja pyyhkiä rätillä pölyjä pois.\nKäytätkö rättiä?\nA = Kyllä\nB = Ei\n")
    while useitemratti != "A" and useitemratti != "B":
        useitemratti = input("Valitse A tai B.\n")
    if useitemratti == "A":
        player_in_room.loseitem(items_dict.get("ratti"))
        player_in_room.mayorpoints += 4
        print("PORMESTARI: 'Olipa mukavasti tehty.\n")
    elif useitemratti == "B":
        player_in_room.mayorpoints -= 1
            
    print("Aika lähteä, Mauri ei ole täällä. Huoneessa on takaovi, josta Pormestari jo sujahtaa ulos.\n")
    nextroom = "room4a"
    player_in_room.move(rooms_dict.get(nextroom))
    return nextroom

def room3a2fun(player_in_room):
    print(f"Saavutte paikkaan {player_in_room.current_room.name}. Mauria ei näy, mutta nurkassa kyhjöttää pieni surkea sardiini lian peitossa.\nNURKKASARDIINI: 'Tulitteko tekin pilkkaamaan minua? Nuoret sardiinit heittivät päälleni jotain tuosta lattialta enkä uskalla poistua...'\n")
    useitemratti2 = input("Pormestarilla on tippa silmäkulmassa. Liikuttaako sinuakin Nurkkasardiinin huono kohtelu?\nKäytätkö rättiä hänen putsaamiseensa?\nA = Kyllä\nB = Ei\n")
    while useitemratti2 != "A" and useitemratti2 != "B":
        useitemratti2 = ("Valitse A tai B!\n")
    if useitemratti2 == "A":
        player_in_room.loseitem(items_dict.get("ratti"))
        player_in_room.mayorpoints += 5
        print("NURKKASARDIINI: 'Kiitos! Kiitos tuhannesti!'\n")
    elif useitemratti2 == "B":
        player_in_room.mayorpoints -= 2
        ("Oletpas pihi kun et rättiä viitsi käyttää!\n")

    print("Aika lähteä, Mauri ei ole täällä. Pormestari ryömii jo ulos vessan ikkunasta kohti levämetsää.\n")
    nextroom = "room4b"
    player_in_room.move(rooms_dict.get(nextroom))
    return nextroom
    

def room4afun(player_in_room):
    print(f"Saavutte paikkaan {player_in_room.current_room.name}. Edessä aukeaa tie, joka johtaa vain yhteen suuntaan.\n")
    if player_in_room.mayorpoints <= 0:
        joke = input("Pormestari vaikuttaa jo kyllästyneen seuraasi.\nKerrotko hänelle vitsin piristääksesi häntä?\nA = Kyllä\nB = Ei\n")
        while joke != "A" and joke != "B":
            joke = input("A vai B?\n")
        if joke == "A":
            print("Pormestari hymyää hiljaa ja saat vahvistuksen, että hän jaksaa matkata kanssasi loppuun saakka.\n")
            player_in_room.mayorpoints += 3
            nextroom = "room5"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom
        elif joke == "B":
            print(f"Pormestari näyttää päättäväiseltä. Hän mulkaisee sinua viimeisen kerran ja juoksee karkuun.\nOlet päässyt velvollisuuksistasi, ja ainoa mitä sinulle jäi käteen (reppuun) on:\n{player_in_room.itemlist}")
            nextroom = "room6a"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom
    else:
        print("Kävelette päättäväisesti tietä pitkin kohti seuraavaa haastetta.\nPormestarin pienillä sardiinin kasvoilla näkyy vaihdellen huolta ja toivoa.\n")
        nextroom = "room5"
        player_in_room.move(rooms_dict.get(nextroom))
        return nextroom

def room4bfun(player_in_room):
    print(f"Saavutte paikkaan {player_in_room.current_room.name}.\nMetsä on pimeä, mutta näet kauempana metsässä valonsäteitä jotka antavat toivoa ettei metsä jatku loputtomiin.\n")
    forestchoice = input("Edessä on kuitenkin paljon matkaa, ja Pormestari vaikuttaa väsyneeltä.\nKannatko Pormestaria?\nA = Kyllä, olen herrasmuikku\nB = En, olen ilkeä\n")
    while forestchoice != "A" and forestchoice != "B":
        forestchoice = input("A vai B...")
    if forestchoice == "A":
        player_in_room.mayorpoints += 4
        print("PORMESTARI: 'Oi kiitos! En toki ole kovin vanha, mutta olen laiska kulkemaan pitkiä matkoja...'\n")
    elif forestchoice == "B":
        print("Ok, laiskuri..\n")
    print("Metsän loppu häämöttää jo, ja pääsette vihdoin tielle joka näkyy johtavan kohti jonkinlaista rakennelmaa.\n")
    nextroom = "room5"
    player_in_room.move(rooms_dict.get(nextroom))
    return nextroom

def room5fun(player_in_room):
    #roommove = {"A": room6bfun, "B": room6afun}
    print(f"Tämäpä erikoista! Saavutte paikkaan {player_in_room.current_room.name}.\nSuuren pesän ovella näkyy Pormestarille tuttu hahmo.\nPORMESTARI: 'Mauri! Pieni rakkaani! Missä olet ollut?'\n")
    print("Kuitenkin nopeasti huomaatte, ettei Mauri ole pieni lainkaan.\nTämä katkarapu on syönyt reilun määrän eikä mahtuisi enää edes kaupungintalon ovesta sisään.\nMauri näkyy myös silmäilevän sinua ja Pormestaria nälkäisesti.\n")
    if items_dict.get("sanakirja") in player_in_room.inventory:
        usesanakirja = input("Mutta sinullahan on mukanasi Sardiini - Katkarapu -sanakirja! Käytätkö sitä Maurille jutteluun?\nA = Kyllä\nB = Ei\n")
        while usesanakirja != "A" and usesanakirja != "B":
            usesanakirja = input("Valitse A tai B....\n")

        if usesanakirja == "A":
            print("Maurin katseeseen tulee nälän sijaan tunnistus ja kaipuu.\nSanakirjan avulla puhuminen on humanisoinut teidät Maurin silmissä.\nMauri suostuu lähtemään Pormestarin mukana kotiin, vaikka hänen täytyykin nyt koostaan johtuen asua pihalla.\n")
            nextroom = "room6b"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom
        
        elif usesanakirja == "B":
            print("Mauri nähtävästi syö Pormestarin.\nEt toki ole aivan varma, koska olet jo lähtenyt juoksemaan kauas pois.\n")
            nextroom = "room6a"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom
            
    elif items_dict.get("pesis") in player_in_room.inventory:
        usepesis = input("Mutta hätä ei ole tämän näköinen, sinulla on pesäpallomaila mukanasi!\nKäytätkö sitä puolustamaan Pormestaria ja itseäsi nälkäiseltä Maurilta?\nA = Kyllä\nB = Ei\n")
        while usepesis != "A" and usepesis != "B":
            usepesis = input("A tai B!!!\n")
        if usepesis == "A":
            print("Mauri on nyt mäskinä, eikä päässyt syömään teitä.\nPormestari näyttää nyt hyvin hyvin surulliselta Maurin kohtalosta.\nLähdette sanattomina eri suuntiin.\n")
            nextroom = "room6a"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom
            
        elif usepesis == "B":
            print("Mauri nähtävästi syö Pormestarin.\nEt toki ole aivan varma, koska olet jo lähtenyt juoksemaan kauas pois.\n")
            nextroom = "room6a"
            player_in_room.move(rooms_dict.get(nextroom))
            return nextroom
            
    elif items_dict.get("avain") in player_in_room.inventory:
        print("Vedät repustasi avaimen. Maurin katse kiinnittyy siihen.\nMAURI: 'blub blub blub???'\nMauri osoittaa oveensa ja tajuat avaimen olevan Maurin uuden kotipesän avain.\n")
        print("PORMESTARI: 'Mauri! Sinähän jätit minulle avaimesi vinkiksi!'\nMauri näyttää tunnistaneen Pormestarin, ja on halukas lähtemään mukananne kaupungintalolle.\n")
        nextroom = "room6b"
        player_in_room.move(rooms_dict.get(nextroom))
        return nextroom

def room6afun(player_in_room):
    print(f"Paikan nimi on {player_in_room.current_room.name}.\nOlet epäonnistunut tehtävässäsi, ja pettänyt Pormestarin.\n\033[1;31mGAME OVER\033[0m")

def room6bfun(player_in_room):
    print("Onnittelut!\nMauri on saatettu kotiin.\nPormestari on heti alkanut laajentamaan kaupungintalon ovea Maurille sopivaksi.")
    if player_in_room.mayorpoints >= 7:
        print("PORMESTARI: 'Kiitos sinulle kaikesta. Olet mahtava tyyppi.\n")
    elif player_in_room.mayorpoints <= 0:
        print("PORMESTARI: 'Kiitos...'\n")
    else:
        print("PORMESTARI: 'Kiitos vain!'\n")
    print("Hyviä tekoja on tehty tänään.\nLähdet tyytyväisin mielin kotiin.\n♡(◔ω◔ )♡\n")

rooms_dict = {"crossing" : Room("Tie risteää", crossing),
    "room1" : Room("Sardiinian Kaupungintalo", meetthemayor),
"room2a" : Room("Pub Sihisevä Sardiini", room2afun, "Rätti"),
"room2b" : Room("Seppo Sardiinin koti", room2bfun),
"room3a1" : Room("Baarin henkilökunnan huone", room3a1fun),
"room3a2" : Room("Baarin vessa", room3a2fun),
"room3b1" : Room("Sardiinitehdas", room3b1fun),
"room3b1b" : Room("Sardiinitehdas (taas)", room3b1bfun),
"room3b2" : Room("Tehtaan konsolihuone", room3b2fun),
"room4a" : Room("Sardiini highway", room4afun),
"room4b" : Room("Levämetsä", room4bfun),
"room5" : Room("Maurin uusi pesä", room5fun),
"room6a" : Room("Epäonnistumisen tyyssija", room6afun),
"room6b" : Room("Hyvä ratkaisu", room6bfun)}