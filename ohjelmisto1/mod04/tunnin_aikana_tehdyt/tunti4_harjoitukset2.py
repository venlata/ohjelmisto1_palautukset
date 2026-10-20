#if / else / elif
luku1=3
luku2=5
if luku2 > luku1:
    print("Moi")
else:
    print("Terve")
#
if luku2 < luku1:
    print("Hej")
else:
    print("Hejdå")
#
vastaus1 = input("Anna jokin luku:\n")
vastaus = int(vastaus1)
if vastaus < 100:
    print(f"Lukusi {vastaus} on pienempi kuin sata!")
elif vastaus == 100:
    print(f"Lukusi {vastaus} on tasan sata :o")
elif vastaus > 1000:
    print("Tuo on jo liian iso luku")
else:
    print(f"Lukusi {vastaus} on isompi kuin sata")
#
vastaus2 = input("Anna joku muu luku:\n")
vastaus3 = int(vastaus2)
print("Ihan ok luku")
#
vastaus5 = int(input("Montako kertaa tervehdimme?\n"))
str1 = "Terve"
print(f'{str1} {vastaus5} kertaa!')
#ˆtuossa ei välttämättä tarvitse edes muuttaa tyyppiä (int)
käyttäjä = input("Anna nimesi: \n")
print(f"Hauska tavata, {käyttäjä}!")
#
#
luku9=9
if 3 <= luku9 <= 11:
    print("Hei")