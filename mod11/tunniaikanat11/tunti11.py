class Viesti:
    lahetetty = 0
    def __init__(self, sisalto):
        Viesti.lahetetty += 1
        self.sisalto = sisalto
    

v1 = Viesti("Hello")
v2 = Viesti("Kauppalista")
v3 = Viesti("Jea")
v4 = Viesti("Apuva")


print(Viesti.lahetetty)

