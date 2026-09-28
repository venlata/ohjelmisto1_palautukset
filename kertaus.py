# with open("instructions.txt", "w") as f:
#     f.write("Testitiedosto, Pythonilla luotu")
#     print(type(f))
#     f.write("\nLisää tekstiä")

# with open("instructions.txt", "a") as f:
#     f.write("\nVielä lisää")

# with open("instructions.txt", "a") as f:
#     f.write("\njne")

# with open("instructions.txt", "r") as f:
#     data = f.read()
#     print(data)

import json

tallennus_data = {
    "pelaaja": "Matti",
    "taso": 5,
    "varusteet": ["miekka", "kilpi", "haarniska"]
}
with open("kertaus.json", "w") as tiedosto:
    json.dump(tallennus_data, tiedosto)

list1 = [2, 6, 'hello', (3, 4), [5, 7]]
with open("kertaus3.json", "w") as tiedosto:
    json.dump(list1, tiedosto)