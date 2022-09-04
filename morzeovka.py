from time import sleep
import winsound
morz=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

x=input("Napiš zprávu kterou chceš přeložit do morzeovy abecedy: ").lower()

for i in x:
    if i==" ":
        print("",end=" |")
        sleep(.5)
        continue
    for j in morz[ord(i)-ord("a")]:
        print(j,end="")
        if j==".":
            winsound.Beep(3000,100)
        else:
            winsound.Beep(3000,300)
    print("|",end="")
