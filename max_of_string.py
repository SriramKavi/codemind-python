a=input()
for i in a :
    m=ord(i)
    break
for j in a :
    if ord(j)>m :
        m=ord(j)
print(chr(m))