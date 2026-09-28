import json


with open("kertaus.json", "r") as tiedosto:
    data_luettu = json.load(tiedosto)
print(f"Pelaaja: {data_luettu['pelaaja']}, taso: {data_luettu['taso']}, varusteet: {data_luettu['varusteet']}")

# Moi 1 kertaa --- Moi 50 kertaa
#save.txt

with open("save.txt", "w") as f:
    for i in range(50):
        f.write(f"Moi {i+1} kertaa!\n")

with open("kertaus3.json", "r") as tiedosto:
    readin = json.load(tiedosto)
print(f"{readin[0]}, {readin[3]}")
