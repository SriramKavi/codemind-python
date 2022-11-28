def cnt(a) :
    c=0
    for i in a :
        if i==" " :
            c=0
            continue
        if i in v :
            c+=1
    return c
a=input()
c=0
k=a.split()
l=[]
v='aeiouAEIOU'
for i in k :
    l.append(cnt(i))
print(*l)
