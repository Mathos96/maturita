from datetime import datetime

print("Napiš své datum narození:")
d=int(input("Den: "))
m=int(input("Měsíc: "))
r=int(input("Rok: "))

now=datetime.today()
date=datetime(r,m,d)
print((now-date).days+1)