tup1 = (3, 5, 8, 10, (24, 25), "Moi", 200)

print(len(tup1))
print(tup1.index(10))

if tup1.count(10) == True:
    print("Numero 10 on siellä")
else:
    print("Ei ole 10 siellä")
#TAI;
print(10 in tup1)

if tup1.count(210) == True:
    print("Numero 210 on siellä")
else:
    print("Ei ole 210 siellä")

tup2 = reversed(tup1)
for tuppeli in tup2:
    print(tuppeli)
