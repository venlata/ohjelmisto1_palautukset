class Item:
    def __init__(self, name, weight=10):
        self.name = name
        self.weight = weight #weight in grams

items_dict = {"sanakirja" : Item("Sanakirja", 20),
              "pesis" : Item("Pesäpallomaila", 200),
              "avain" : Item("Avain", 4),
              "ratti" : Item("Rätti", 3),
              "juoma" : Item("Juomapullo"),
              "kivi" : Item("Kivi", 1)}