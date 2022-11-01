n=int(input())
l=list(map(int,input().split()))[:n]
k=[]
for i in range(len(l)) :
    if l[i]%2==0 :
        k.append(i)
print(max(k))
