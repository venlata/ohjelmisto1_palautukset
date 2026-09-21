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

class EV(Auto):
    def __init__(self, regno, maxspeed, currentspeed, mileage, kwh):
        super().__init__(regno, maxspeed, currentspeed, mileage)
        self.kwh = kwh
    def trip(self, hours):
        return super().trip(hours)
    def speeding(self, change):
        return super().speeding(change)

class GV(Auto):
    def __init__(self, regno, maxspeed, currentspeed, mileage, tank):
        super().__init__(regno, maxspeed, currentspeed, mileage)
        self.tank = tank
    def trip(self, hours):
        return super().trip(hours)
    def speeding(self, change):
        return super().speeding(change)

ev1 = EV("ABC-15", 180, 0, 0, 52.5)
gv1 = GV("ACD-123", 165, 0, 0, 32.3)

ev1.speeding(46)
gv1.speeding(66)
ev1.trip(3)
gv1.trip(3)

print(f"{ev1.regno}: {ev1.mileage}\n{gv1.regno}: {gv1.mileage}")
# autos = []
# maara = 1

# while maara <= 10:
#     regn = f"ABC-{maara}"
#     maxispeed = random.randint(100,200)
#     cname = f"auto{maara}"
#     cname = Auto(regn, maxispeed, 0, 0)
#     autos.append(cname)
#     maara += 1


# onkaynnis = True
# class Competish:
#     def __init__(self, comname, kilometers, vehiclelist = autos):
#         self.comname = comname
#         self.kilometers = kilometers
#         self.vehiclelist = autos
#     def onehourlater(self):
#         onkaynnis = True
#         while onkaynnis:
#             for item in autos:
#                 if item.mileage < self.kilometers:
#                     item.speeding(random.randint(-10,15))
#                     item.trip(1)
#                 if item.mileage >= self.kilometers:
#                     print(f"Auto {item.regno} on ekana maalissa kilsoilla {item.mileage}!")
#                     onkaynnis = False
#             if not onkaynnis:
#                 break

# c1 = Competish("Kilpailu1", 8000)
# c1.onehourlater()
# print("Kilpailun lopputulos:")
# for item in autos:
#     print(f"Auto:{item.regno}, Nopeus: {item.currentspeed}, Max. nopeus: {item.maxspeed}, Kuljettu matka: {item.mileage}")

