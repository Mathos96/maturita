x=input("Zadej rodné číslo: ")

if len(x)!=10:
    print("Špatná délka!")
    exit()

if int(x[2:4]) in range(51,62):
    print("Žena")
else:
    print("Muž")

sumas=sum(map(int,x[::2]))
sumal=sum(map(int,x[1::2]))

if (sumas-sumal)%11==0:
    print("Platné!")
else:
    print("Neplatné!")
