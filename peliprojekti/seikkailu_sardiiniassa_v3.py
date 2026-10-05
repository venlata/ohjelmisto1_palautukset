import random
import json

from items import items_dict
from rooms import rooms_dict
from rooms import meetthemayor
from rooms import mainmenu
from player import Player

with open("./peliprojekti/intro.txt", "r") as tiedosto:
    data = tiedosto.read()
    print(data)

try:
    ohjeet = input("Haluatko ohjeet? [y/n]\n")
except ValueError:
    print("Vastaus ei ollut y tai n\n")
if ohjeet == "y":
    with open("./peliprojekti/ohjeet.txt", "r") as tiedosto:
        data = tiedosto.read()
        print(data)

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

#Tallennusdatan kanssa piti kikkailla koska json ei osaa lukea hassuja objekteja.
def save_game(player_name, player_age, room_name, player_inventory, player_mayorpoints):
    tallennus_data = {"player": player_name,
                      "age": player_age,
                      "room": room_name,
                      "inventory": [item.name for item in player_inventory],
                      "mayorpoints": player_mayorpoints}

    with open("./peliprojekti/save.json", "w", encoding="utf-8") as tiedosto:
        json.dump(tallennus_data, tiedosto)
    with open("./peliprojekti/save.json", "r") as tiedosto:
        data_luettu = json.load(tiedosto)
    print(f"Pelaaja: {data_luettu["player"]}, ikä: {data_luettu["age"]} huone: {data_luettu["room"]}, varusteet: {data_luettu["inventory"]}")


meetthemayor(player1)
mainmenu(player1)
room = rooms_dict.get("crossing")
#Peli alkaa kunnolla ensimmäisestä risteyksestä. Loop kutsuu aina nextroomia, joka määritellään edellisessä huoneessa valintojen mukaan.
while True:
    nextroom = room.play_room(player1)
    save_game(player1.name, player1.age, room.name, player1.inventory, player1.mayorpoints)
    try:
        menyy = input("Haluatko katsoa ystävyyspisteesi Pormestarin kanssa? [y/n]\n")
        if menyy == "y":
            print(f"Pisteesi: {player1.mayorpoints}\n")
        
    except ValueError:
        continue
    if nextroom == None:
        break
    #Peli päättyy kun seuraavia huoneita ei enää ole.
    room = rooms_dict.get(nextroom)


