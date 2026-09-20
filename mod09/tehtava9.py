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

    


auto0 = Auto("ABC-123", 142, 0, 0)

auto0.speeding(30)
auto0.trip(2.5)

print(f"{auto0.regno}\nMaksiminopeus: {auto0.maxspeed}km/h\nTämänhetkinen nopeus: {auto0.currentspeed}km/h\nMittarilukema: {auto0.mileage}")

auto0.speeding(70)
auto0.speeding(50)
auto0.trip(1.7)

print(f"{auto0.regno}\nMaksiminopeus: {auto0.maxspeed}km/h\nTämänhetkinen nopeus: {auto0.currentspeed}km/h\nMittarilukema: {auto0.mileage}")

auto0.speeding(-200)

print(f"{auto0.regno}\nMaksiminopeus: {auto0.maxspeed}km/h\nTämänhetkinen nopeus: {auto0.currentspeed}km/h\nMittarilukema: {auto0.mileage}")

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
while onkaynnis:
    for item in autos:
        if item.mileage < 10000:
            item.speeding(random.randint(-10,15))
            item.trip(1)
        if item.mileage >= 10000:
            print(f"Auto {item.regno} on ekana maalissa kilsoilla {item.mileage}!")
            onkaynnis = False
    if not onkaynnis:
        break
    
print("Kilpailun lopputulos:")
for item in autos:
    print(f"Auto:{item.regno}, Nopeus: {item.currentspeed}, Max. nopeus: {item.maxspeed}, Kuljettu matka: {item.mileage}")
