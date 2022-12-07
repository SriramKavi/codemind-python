def fact(a) :
    fs=0
    for i in range(1,a+1) :
        if a%i==0 :
            fs+=i
    return fs

l=list(map(int,input().split(',')))
c=0
k=[]
for i in l :
    if fact(i) in l :
        c+=1
        k.append(i)

k.sort()
if c!=0 :
    
    print(*k)
else :
    print('-1')
