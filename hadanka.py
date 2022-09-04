from random import randrange

urovne=[20,50,100,200]

for i in range(len(urovne)):
    print("Úroveň: "+str(i+1))
    print("Interval: [1-"+str(urovne[i])+"]")
    r=randrange(urovne[i])
    #print(r) #cheat
    hp=7
    while hp>0:
        x=int(input("Hadej [HP:"+str(hp)+"/7]: "))
        if x<1 or x>urovne[i]:
            print("Cislo je mimo hraci interval!")
            continue
        if x<r:
            print("Hadane cislo je vetsi!")
            hp=hp-1
            continue
        else:
            if x>r:
                print("Hledane cislo je mensi!")
                hp=hp-1
                continue
            else:
                print("Vyhra!!!!")
                break
    if hp==0:
        print("Konec hry")
        exit()

print("Vyhral jsi celou hru gratuluji!")

