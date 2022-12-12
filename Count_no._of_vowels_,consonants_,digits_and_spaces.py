a=input()
v='aeiouAEIOU'
vc=0
cn=0
d=0
sp=0
for i in a :
    if ord(i)>=48 and ord(i)<=57 :
        d+=1
    elif i in v :
        vc+=1
    elif ord(i)==32 :
        sp+=1
    else :
        cn+=1
print("Vowels:",vc)
print("Consonants:",cn)
print("Digits:",d)
print("White spaces:",sp)