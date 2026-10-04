import random

#Tarvitaan kaikille optioille: errorviestin (tyhjä kenttä) proofing, 
# tallennustoiminto, toiminto jotta voi komennolla tsekkaa mayorpoints 
from items import items_dict
from rooms import rooms_dict
from rooms import meetthemayor
from rooms import mainmenu
from player import Player



playername = input("Mikä on nimesi?\n")
playerage = int(input("Mikä on ikäsi?\n"))
while True:
    if playerage < 12:
        print("Annoitko ikäsi vahingossa planktonvuosissa vai oletko vain noin nuori??? Tänne ei pieniä lapsia haluta!\n")
        playerage = int(input("Mikä on ikäsi?\n"))
    else:
        player1 = Player(playername, playerage)
        
        print(f"\nHei {playername}, {playerage}v. Tervetuloa Sardiiniaan!\nOlet nyt muikku, ja paikassa Sardiinian Kaupungintalo.\n")
        break

meetthemayor(player1)
mainmenu(player1)
room = rooms_dict.get("crossing")
while True:
    nextroom = room.play_room(player1)
    print("DEBUG: nextroom ", nextroom)
    if nextroom == None:
        break
    room = rooms_dict.get(nextroom)
    print("DEBUG: room.name ", room.name)


    
    




