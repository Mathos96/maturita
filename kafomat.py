cena=int(input("Zadej cenu napoje: "))
penize=int(input("Vložené peníze: "))

bankovky=[5000,2000,1000,500,200,100,50,20,10,5,2,1]

if penize<cena:
    print("Nedostatek peněz!")
    exit()

if penize==cena:
    print("Nic ti nevrátím!")
    exit()

penize=penize-cena
print("Vrátím ti: "+str(penize)+"Kč")
for b in bankovky:
    if penize//b>0:
        print(str(penize//b)+"x"+str(b)+"Kč")
        penize=penize-(penize//b)*b


