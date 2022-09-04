mes=[31,29,31,30,31,30,31,31,30,31,30,31]
mesice=["leden","únor","březen","duben","květen","červen","červenec","srpen","září","říjen","listopad","prosinec"]

while True:
    print("1.) Číslo dne")
    print("2.) Den + měsíc")
    print("3.) Konec")
    try:
        x=int(input())
    except:
        print("Zadal jsi něco co není povolené!")
        continue
    if not x in range(1,4):
        print("Zadal jsi něco co není povolené!")
        continue
    if x==3:
        exit()
    if x==1:
        c=int(input("Zadej číslo v rozsahu 1-366: "))
        if not c in range(1,367):
            print("Zadal jsi něco mimo rozsah!")
            continue
        m=1
        i=0
        while c>mes[i]:
            c-=mes[i]
            i+=1
        print(str(c)+". "+mesice[i])
    if x==2:
        d=int(input("Zadej číslo v rozsahu 1-31: "))
        if not d in range(1,32):
            print("Zadal jsi něco mimo rozsah!")
            continue
        m=int(input("Zadej číslo v rozsahu 1-12: "))
        if not m in range(1,13):
            print("Zadal jsi něco mimo rozsah!")
            continue
        c=d
        for i in range(m-1):
            c+=mes[i]
        print(c)
    