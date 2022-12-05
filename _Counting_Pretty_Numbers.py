def pretty(a) :
    r=a%10
    return r


t=int(input())
k=[]
for i in range(t) :
    l,r=map(int,input().split())
    c=0
    for j in range(l,r+1) :
        if pretty(j)==2 or pretty(j)==3 or pretty(j)==9 :
            c+=1
    print(c)
