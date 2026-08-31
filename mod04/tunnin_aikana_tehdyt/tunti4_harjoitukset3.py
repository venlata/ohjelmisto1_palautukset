ikä = int(input("Anna ikäsi: "))
if ikä >= 65:
    print("Olet eläkeiässä.")
elif ikä >= 18:
    print("Olet työiässä.")
elif ikä >= 7:
    print("Olet koululainen.")
else:
    print("Olet pikkulapsi.")

lampo=int(input("Mikä on lämpötila? \n"))
if lampo >= 25:
    print("Tosi lämmin")
elif 15 <= lampo <= 24:
    print("Mahtavaa!")
elif 10 <= lampo <=14:
    print("Ihan ok")
elif 0 <= lampo <= 9:
    print("Vähän kylmä")
else:
    print("Tosi kylmä!")

lukusi = int(input("Anna luku: \n"))
if 10 <= lukusi <= 20:
    print(f"Lukusi {lukusi} on 10 ja 20 välillä!")
else:
    print(f"Lukusi {lukusi} on välin ulkopuolella")

#ohjelma joka kertoo onko luku pariton tai parillinen (jakojäännöksellä):

parluku = int(input("Anna luku: \n"))
if parluku % 2 == 0:
    print(f"Lukusi {parluku} on parillinen")
else:
    print(f"Lukusi {parluku} on pariton")