class Viesti:
    lahetetty = 0
    def __init__(self, sisalto):
        Viesti.lahetetty += 1
        self.sisalto = sisalto
    

v1 = Viesti("Hello")
v2 = Viesti("Kauppalista")
v3 = Viesti("Jea")
v4 = Viesti("Apuva")


# print(Viesti.lahetetty)

class Animal:
    def __init__(self, paino):
        self.paino = paino

    def kavelee(self):
        print("Eläin kävelee")

class Dog(Animal):
    def __init__(self, paino, hanta):
        super().__init__(paino)
        self.hanta = hanta

    def kavelee(self):
        super().kavelee()
        print("Koira kävelee")

d1 = Dog(24, "ruma häntä")

# d1.kavelee()

class Shape:
    def __init__(self, colour):
        self.colour = colour

    def measure(self, rectangle):
        print(f"Nyt lasken piirin...")

class Rectangle(Shape):
    def __init__(self, colour, length, width):
        super().__init__(colour)
        self.length = length
        self.width = width

    def measure(self):
        piiri = 2 * (self.length + self.width)
        super().measure(self)
        print(piiri)

m1 = Shape("sininen")

sk1 = Rectangle("punainen", 25, 40)

sk1.measure()
