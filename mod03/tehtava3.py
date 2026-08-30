import math
import random
#Tehtävä 3 osa 1
nimesi = input("Kerro nimesi:\n")
print(f"Terve, {nimesi}!\n")

#Tehtävä 3 osa 2
sade = float(input("Kerro ympyräsi säde:\n"))
print(f"Ympyräsi pinta-ala on {math.pi * (sade * sade):.2f}.\n")

#Tehtävä 3 osa 3
kanta = float(input("Kerro suorakulmiosi kanta (metreissä):\n"))
korkeus = float(input("Kerro suorakulmiosi korkeus (metreissä):\n"))
print(f"Suorakulmiosi pinta-ala on {(kanta) * (korkeus): .0f}mˆ2.")
print(f"Suorakulmiosi piiri on {(kanta)+(kanta)+(korkeus)+(korkeus):.0f}m.\n")

#Tehtävä 3 osa 4
luku1, luku2, luku3 = list(map(int,input("Anna kolme lukua:\n").split( )))
summa = luku1 + luku2 + luku3
print(f"Lukujesi summa: {summa}")
print(f"Lukujesi tulo: {(luku1)*(luku2)*(luku3)}")
print(f"Lukujesi keskiarvo: {(summa)/(3):.2f}\n")

#Tehtävä 3 osa 5
luoti = 13.3
naula = 425.6
leiviska = 8512
leiviskat = float(input("Anna leiviskät:\n"))
naulat = float(input("Anna naulat:\n"))
luodit = float(input("Anna luodit:\n"))
luoditg = luoti * luodit
naulatg = naula * naulat
leiviskatg = leiviska * leiviskat
grammat = leiviskatg + luoditg + naulatg
print(f"Massa nykymittojen mukaan: {(grammat)/(1000):.0f}kg ({(grammat):.0f}g)\n")

#Tehtävä 3 osa 6
num1 = str(random.randint (1,9))
num11 = str(random.randint (1,9))
num111 = str(random.randint (1,9))
num2 = str(random.randint (1, 6))
num22 = str(random.randint (1, 6))
num222 = str(random.randint (1, 6))
num2222 = str(random.randint (1, 6))
print (f"Lukon numerokoodi kolmella numerolla: {num1 + num11 + num111}")
print (f"Lukon numerokoodi neljällä numerolla: {num2 + num22 + num222 + num2222}\n")
# ei ole kaunis mutta toimii :D