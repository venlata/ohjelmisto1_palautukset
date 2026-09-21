#Tehtävä 10

class Hissi:
    def __init__(self, topfloor, bottomfloor, current = 1):
        self.topfloor = topfloor
        self.bottomfloor = bottomfloor
        self.current = current

    def up(self):
        target = self.current + 1
        if self.topfloor >= target >= self.bottomfloor:
            self.current += 1
        

    def down(self):
        target = self.current - 1
        if self.topfloor >= target >= self.bottomfloor:
            self.current -= 1
        

    def moveto(self, cfloor):
        while self.current != cfloor:
            if self.current > cfloor:
                self.down()
            if self.current < cfloor:
                self.up()
            else:
                return self.current
                


hissi1 = Hissi(12, -1)

hissi1.moveto(5)
print(hissi1.current)
hissi1.moveto(-1)
print(hissi1.current)

class House:
    def __init__(self, lowfloor, upfloor, elevators):
        self.lowfloor = lowfloor
        self.upfloor = upfloor
        self.elevators = []

    def drive_elevator(self, elnumber, targetfloor):
        elnumber = elnumber -1
        elv = self.elevators[elnumber]
        elv.moveto(targetfloor)

    def alarm(self):
        self.moveto(self.bottomfloor)


houselist = []
print("Luo talo!\nAnna ensimmäisen kysymyksen vastaukseksi 0 kun alkaa olla tarpeeksi monta.")
while True:
    creationlow = int(input("Anna talon alimman kerroksen numero: "))
    creationhigh = int(input("Anna talon ylimmän kerroksen numero: "))
    creationelev = int(input("Anna hissien lukumäärä: "))
    newhouse = House(creationlow, creationhigh, creationelev)
    houselist.append(newhouse)
    for hissit in range(creationelev):
        newelevator = Hissi(creationhigh, creationlow)
        newhouse.elevators.append(newelevator)
    if creationlow == 0:
        break

for item in newhouse.elevators:
    print(f"Hissin ylin kerros: {item.topfloor}, Hissin alin kerros: {item.bottomfloor}")

for item in houselist:
    print(f"Talon alin kerros: {item.lowfloor} Talon ylin kerros: {item.upfloor}")
    for hissi in item.elevators:
        print(f"Hissin ylin kerros: {hissi.topfloor}, Hissin alin kerros: {hissi.bottomfloor}")


drivin = int(input("Minkä talon hissiä haluat ajaa (numero)? "))
drivin -= 1
elly = int(input("Mitä hissiä haluat ajaa? "))
floor = int(input("Mihin kerrokseen haluat? "))
houselist[drivin].drive.elevator(elly, floor)
#En nyt keksi miten kutsua tuota taloa :(
