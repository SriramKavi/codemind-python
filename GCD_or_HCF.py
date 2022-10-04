def hcf(n,m) :
    dn=list()
    dm=list() 
    for i in range(1,n+1):
        if n%i==0 :
            dn.append(i)
    for j in range(1,m+1):
        if m%j==0 :
            dm.append(j)
    l=list()
    for i in dn :
        for j in dm :
            if i==j :
                l.append(i)
    print(max(l))

n,m=map(int,input().split())
hcf(n,m)

