from random import randrange

cesky=["jablko","auto","dům","stůl","myš","hodiny","červená","světlo","čas","zelená","kůň","cibule","rajče","brambora","koláč","duch","výtah","klávesnice","vesmír","liška"]
anglicky=["apple","car","house","table","mouse","clock","red","light","time","green","horse","onion","tomato","potato","pie","ghost","elevator","keayboard","space","fox"]

pocet=len(cesky)
delka=10 #delka testu<pocet slov
body=0
q=0
a=[0,0,0]
for i in range(delka):
    a[0]=a[1]
    while a[0]==a[1] or a[1]==a[2] or a[2]==a[0]:
        a[0]=randrange(pocet)
        a[1]=randrange(pocet)
        a[2]=randrange(pocet)
    s=randrange(3)
    print("Otázka ("+str(i+1)+"/"+str(delka)+"):")
    print("Přelož: "+anglicky[a[s]])
    print()
    for j in range(3):
        print(str(j+1)+": "+cesky[a[j]])
    
    ans=int(input("Odpověď: "))
    if ans==s+1:
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
