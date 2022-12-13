a=input()
c=0
for i in a :
    if ord(i)>=48 and ord(i)<=57 :
        c+=1
if c!=0 :
    print("Contains",c,"digit")
else :
    print("Doesn't contain digit")