def lcm(a,b) :
    ma=list()
    mb=list()
    k=list()
    for i in range(1,50):
        ma.append(a*i)
    for j in range(1,50):
        mb.append(b*j)
    for n in ma :
        for m in mb :
            if n==m :
                k.append(n)
    print(min(k))
                


a,b=map(int,input().split())
lcm(a,b)
