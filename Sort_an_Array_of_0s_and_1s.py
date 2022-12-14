n=int(input())
l=list(map(int,input().split()))[:n]
c=[]
c1=[]
for i in l :
    if i==0 :
        c.append(i)
    elif i==1 :
        c1.append(i)
c.extend(c1)
print(*c)
    
