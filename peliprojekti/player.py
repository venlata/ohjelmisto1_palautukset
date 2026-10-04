class Player:
    def __init__(self, name, age, current_room=None, mayorpoints = 0):
        self.name = name
        self.age = age
        self.inventory = []
        self.current_room = current_room #muokattu: current_room nimeksi, kuvaavampi
        self.mayorpoints = mayorpoints
        self.visited_rooms = []

    def move(self, room):
        self.current_room = room
        self.visited_rooms.append(room.name)
    def collectitem(self, item):
        self.inventory.append(item)
        print(f"Reppuun lisättiin: {item.name}\n")
    def loseitem(self, item):
        self.inventory.remove(item)
        print(f"Repusta lähti: {item.name}\n")
    def itemlist(self):
        print("Repussa on nyt:")
        for i in self.inventory:
            print(i.name)
