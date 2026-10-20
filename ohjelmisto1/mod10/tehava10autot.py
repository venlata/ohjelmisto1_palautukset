import random

class Auto:
    def __init__(self, regno, maxspeed, currentspeed, mileage):
        self.regno = regno
        self.maxspeed = maxspeed
        self.currentspeed = currentspeed
        self.mileage = mileage

    def speeding(self, change):
        self.currentspeed += change
        if self.currentspeed < 0:
            self.currentspeed = 0
        elif self.currentspeed > self.maxspeed:
            self.currentspeed = self.maxspeed
        return self.currentspeed
    
    def trip(self, hours):
        if self.currentspeed > 0:
            self.mileage += hours * self.currentspeed
        else:
            self.mileage += 0



autos = []
maara = 1

while maara <= 10:
    regn = f"ABC-{maara}"
    maxispeed = random.randint(100,200)
    cname = f"auto{maara}"
    cname = Auto(regn, maxispeed, 0, 0)
    autos.append(cname)
    maara += 1


onkaynnis = True
class Competish:
    def __init__(self, comname, kilometers, vehiclelist = autos):
        self.comname = comname
        self.kilometers = kilometers
        self.vehiclelist = autos
    def onehourlater(self):
        onkaynnis = True
        while onkaynnis:
            for item in autos:
                if item.mileage < self.kilometers:
                    item.speeding(random.randint(-10,15))
                    item.trip(1)
                if item.mileage >= self.kilometers:
                    print(f"Auto {item.regno} on ekana maalissa kilsoilla {item.mileage}!")
                    onkaynnis = False
            if not onkaynnis:
                break

c1 = Competish("Kilpailu1", 8000)
c1.onehourlater()
print("Kilpailun lopputulos:")
for item in autos:
    print(f"Auto:{item.regno}, Nopeus: {item.currentspeed}, Max. nopeus: {item.maxspeed}, Kuljettu matka: {item.mileage}")



#Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, 
# jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. 
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan 
# ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

#tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
#  eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
#tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
#kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa 
# eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
#Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä “Suuri romuralli”. 
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. 
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, 
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. 
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein 
# sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

