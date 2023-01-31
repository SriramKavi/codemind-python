n=int(input())
l=list(map(int,input().split()))[:n]
s=''
for i in l :
        s+=str(i)
s=int(s)+1
k=[]
while s :
    r=s%10
    if r==0 :
        k.append(0)
    else :
        k.append(r)
    s//=10
p=[]
for j in k[-1:-(len(k)+1):-1] :
    p.append(j)
print(*p)
