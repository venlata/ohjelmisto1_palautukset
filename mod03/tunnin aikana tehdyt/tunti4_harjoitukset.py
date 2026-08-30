import math
#Tehtäviä tunnille 4
mu1 = 3
mu2 = 3.5
mu3 = "moi"
mu4 = True
#Tyypin tsekkaus:
print(type(mu1))
print(type(mu2))
print(type(mu3))
print(type(mu4))
#Tässä vaiheessa asensin thonny.app ja laitoin seuraavat:
#k = (17)
#print(k)
#k = muistipaikka johon 17 on laitettu
#print(k) ensin hakee k:n muistista, avaa sen ja asettaa 17 paikalleen printtiin
#ainakin jotenkin näin opettaja selitti asian
#oliko thonny tarpeellinen tälle testille ?
#
#Lukuihin voi asettaa visuaalisen selkeyden vuoksi alaviivoja erottelemaan:
isoluku = 4738_92498_3938747_32211
print(isoluku)
#Obkjektin voi kopioida & muuttaa tyypin
mu1_1 = float(mu1)
print(type(mu1_1))
#Printtitulos kertoo True tai False kun teet statementin:
print(2 < 3)
print(3 < 1)
#Samalle riville voi laittaa useamman muuttujan tiedot pilkulla erotellen:
a, b=3, 6
print(a < b)
#Voi olla ettei ole kovin fiksua jos muuttujien tietoja pitää vaihtaa tulevaisuudessa
#
#jos haluat tehdä statementin jossa on yhtäsuuri, yksi = ei riitä koska = on käsky, ei kysymys
print(2==2)
#jos on 2 statementtia samassa, jos toinen on väärin, vastaus on vain False
print(2==2 and 3<2)
#jos taas haluat tietää vain onko jompi kumpi oikein, käytä or:
print(2==2 or 3<2)
#
print(2!=2)
#
print(not 2==2)
#
#/ jakaa niin että lopputulos voi olla int, // jakaa mutta lopputulos on float
luku1=2
luku2=10
print(luku2/luku1)
print(luku2//luku1)
#f-string formatoi tulokset, esim. kahden desimaalin tarkkuudelle:
print(f'{math.sqrt(luku2):.2f}')
#tai pilkottuna
neliojuuri = math.sqrt(luku2)
print(f'{neliojuuri:.3f}')
#neliöjuuri on myös *luku* potenssiin 0,5
#logaritmi10:
luku3=100
luku4=523
print(f'{math.log10(luku3):.2f}')
print(f'{math.log10(luku4):.2f}')
#
#
if luku1 < luku2:
    print("moi!")
    
