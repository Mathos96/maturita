from random import randrange

staty=["Česká republika","Slovensko","Německo","Polsko","Rakousko","Velká británie","Itálie","Španělsko","Maďarsko","Ukrajina","Belgie","Japonsko","Jižní Korea","Irsko","Island","Bangladéž","Bělorusko","Čína","Francie","Dánsko"]
mesta=["Praha","Bratislava","Berlín","Varšava","Vídeň","Londýn","Řím","Madrid","Budapešť","Kyjev","Brusel","Tokio","Soul","Dublin","Reykjavík","Dháka","Minsk","Peking","Paříž","Kodaň"]

pocet=len(staty)
delka=10 #delka testu<pocet slov
body=0
q=0
a=[0,0,0,0]
for i in range(delka):
    a[0]=a[1]
    while a[0]==a[1] or a[1]==a[2] or a[2]==a[3] or a[3]==a[0]:
        a[0]=randrange(pocet)
        a[1]=randrange(pocet)
        a[2]=randrange(pocet)
        a[3]=randrange(pocet)
    s=randrange(4)
    print("Otázka ("+str(i+1)+"/"+str(delka)+"):")
    print("Přelož: "+staty[a[s]])
    print()
    for j in range(4):
        print(chr(j+ord("a"))+": "+mesta[a[j]])
    
    ans=input("Odpověď: ")
    while ans!="a" and ans!="b" and ans!="c" and ans!="d":
        print("Neplatný vtup!")
        input()
        print("Přelož: "+staty[a[s]])
        print()
        for j in range(4):
            print(chr(j+ord("a"))+": "+mesta[a[j]])
        ans=input("Odpověď: ")

    if ord(ans)-ord("a")==s:
        body=body+1
        print("Správně!")
    else:
        print("Špatně!")
    print()
    print()

print("--------------------------------------------------")
print("Celkový počet bodů: "+str(body)+"/"+str(delka))
if body in range(0,2): 
    print("Výsledná známka je: 5")
if body in range(2,4): 
    print("Výsledná známka je: 4")
if body in range(4,7): 
    print("Výsledná známka je: 3")
if body in range(7,9): 
    print("Výsledná známka je: 2")
if body in range(9,11): 
    print("Výsledná známka je: 1")
