import random
import json

from items import items_dict
from rooms import rooms_dict
from rooms import meetthemayor
from rooms import mainmenu
from player import Player

def venlan_input(prompt, err_msg):
    while True:
        try:
            res = input(prompt)
            return res
        except ValueError:
            print(err_msg)
            continue

def load_game():
    with open("./peliprojekti/save.json", "r") as tiedosto:
        data_luettu = json.load(tiedosto)
        print(f"Pelaaja: {data_luettu["player"]}, ikä: {data_luettu["age"]} huone: {data_luettu["room"]}, varusteet: {data_luettu["inventory"]}")
    currentroom = data_luettu["room_key"]
    print(f"Huone: {currentroom}")
    nextroom = rooms_dict.get(currentroom)
    player = Player(data_luettu["player"],
                    data_luettu["age"],
                    rooms_dict.get(data_luettu["room_key"]),
                    data_luettu["mayorpoints"])
    items_by_name = {item.name: item for item in items_dict.values()}
    player.inventory = [items_by_name[item_name] for item_name in data_luettu["inventory"]]
    player.visited_rooms = data_luettu["visitedrooms"]
    print("Peli jatkuu!\n")
    return (nextroom, player)
   
with open("./peliprojekti/intro.txt", "r") as tiedosto:
    data = tiedosto.read()
    print(data)

ohjeet = venlan_input("Haluatko ohjeet? [y/n]\n", "Vastaus ei ollut y tai n\n")

if ohjeet == "y":
    with open("./peliprojekti/ohjeet.txt", "r") as tiedosto:
        data = tiedosto.read()
        print(data)


#Tallennusdatan kanssa piti kikkailla koska json ei osaa lukea hassuja objekteja.
def save_game(player_name, player_age, room_key, room_name, player_inventory, player_mayorpoints, visited_rooms):
    tallennus_data = {"player": player_name,
                      "age": player_age,
                      "room_key": room_key,
                      "room": room_name,
                      "inventory": [item.name for item in player_inventory],
                      "mayorpoints": player_mayorpoints,
                      "visitedrooms": visited_rooms}

    with open("./peliprojekti/save.json", "w", encoding="utf-8") as tiedosto:
        json.dump(tallennus_data, tiedosto)
    with open("./peliprojekti/save.json", "r") as tiedosto:
        data_luettu = json.load(tiedosto)
    print(f"Pelaaja: {data_luettu["player"]}, ikä: {data_luettu["age"]} huone: {data_luettu["room"]}, varusteet: {data_luettu["inventory"]}")

new_game_or_old_game = venlan_input("Haluatko jatkaa keskeytettyä peliä? [y/n]\n", "")

#Ekana heti ohjeiden saannin jälkeen voit valita jatkatko aiempaa peliä vai aloitatko uuden.
if new_game_or_old_game == "y":
    (room, player1) = load_game()
    print(f"Ladattu pelaaja: {player1.name}, {player1.mayorpoints} Pormestaripistettä")
else:
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
#Peli alkaa kunnolla ensimmäisestä risteyksestä. Loop kutsuu aina nextroomia, joka määritellään edellisessä huoneessa valintojen mukaan.
while True:
    nextroom = room.play_room(player1)
    try:
        menyy = input("Haluatko:\nA = katsoa ystävyyspisteesi Pormestarin kanssa\nB = keskeyttää pelin\nAnna enter tai jokin muu vastaus jatkaaksesi normaalisti\n")
        if menyy == "A":
            print(f"Pisteesi: {player1.mayorpoints}\n")
        elif menyy == "B":
            save_game(player1.name, player1.age, nextroom, room.name, player1.inventory, player1.mayorpoints, player1.visited_rooms)
            print("Peli tallennettu\n")
            break
        
    except ValueError:
        continue
    if nextroom == None:
        break
    #Peli päättyy kun seuraavia huoneita ei enää ole.
    room = rooms_dict.get(nextroom)


