#Tehtävä 11

#Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. 
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, 
# kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat. 
# Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot. 
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). 
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

leh1 = Lehti("Aku Ankka", "Aki Hyyppä")
kir1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

print(f"{leh1.nimi}, {leh1.paatoimittaja}")
print(f"{kir1.nimi}, {kir1.kirjoittaja}, {kir1.sivumaara}")