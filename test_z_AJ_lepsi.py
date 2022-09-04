from random import randrange

cesky=["jablko","auto","dům","stůl","myš","hodiny","červená","světlo","čas","zelená","kůň","cibule","rajče","brambora","koláč","duch","výtah","klávesnice","vesmír","liška"]
anglicky=["apple","car","house","table","mouse","clock","red","light","time","green","horse","onion","tomato","potato","pie","ghost","elevator","keayboard","space","fox"]

pocet=len(cesky)
delka=10 #delka testu<pocet slov
body=0
q=[i for i in range(pocet)]
for i in range(100): #shuffle
    r1=randrange(pocet)
    r2=randrange(pocet)
    tmp=q[r1]
    q[r1]=q[r2]
    q[r2]=tmp
a=[0,0,0]
for i in range(delka):
    a[0]=a[1] #at se znova promichaji potencialni odpovedi
    while a[0]==a[1] or a[1]==a[2] or a[2]==a[0]: #tri navzajem ruzna nahodna cisla
        a[0]=q[i]
        a[1]=randrange(pocet)
        a[2]=randrange(pocet)
    v=[j for j in range(3)]
    for k in range(10): #shuffle
        r1=randrange(3)
        r2=randrange(3)
        tmp=v[r1]
        v[r1]=v[r2]
        v[r2]=tmp
    #s=randrange(3)
    print("Otázka ("+str(i+1)+"/"+str(delka)+"):")
    print("Přelož: "+anglicky[a[0]])
    print()
    for j in range(3):
        print(str(j+1)+": "+cesky[a[v[j]]])
    
    ans=int(input("Odpověď: "))
    if v[ans-1]==0:
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
