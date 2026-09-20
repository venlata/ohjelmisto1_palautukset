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
    
#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. 
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. 
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. 
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. 
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

