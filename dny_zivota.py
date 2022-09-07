x=input("Zadej své datum narození ve formátu DDMMRRRR: ")

mes=[31,28,31,30,31,30,31,31,30,31,30,31]

d=int(x[0:2])
m=int(x[2:4])
r=int(x[4:])

#1.1.1900 bylo pondeli btw!

td=8 #tento den
tm=9 #tento mesic
tr=2022 #tento rok

dnes=td #dny/dnesni datum
dnes+=sum(mes[:tm-1]) #dny v mesicich
dnes+=365*tr #dny za roky

tenkrat=d #dny/datum narozeni
tenkrat+=sum(mes[:m-1]) #dny v mesicich
tenkrat+=365*r #dny za roky

tp=((tr-1)//4)-((tr-1)//100)+((tr-1)//400) #dny za prestupne minule roky, ale bez tohoto proto -1
p=(r//4)-(r//100)+(r//400) #dny za prestupne minule roky
p=tp-p #pocet prestupnych roku (prestupnych dni)

if ((r%4==0 and r%100!=0) or r%400==0): #kdyz je rok narozeni prestupny
    if m<3:     #a jeste neskoncil unor
        p+=1    #tak pridat den bo by chybel

if ((tr%4==0 and tr%100!=0) or tr%400==0): #kdyz je tento rok prestupny
    if tm<3:    #a jeste neskoncil unor tak nebylo 29. unora
        p-=1    #takze odebrat den na tento prestupny rok

print(dnes-tenkrat+p)

