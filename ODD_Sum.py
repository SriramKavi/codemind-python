n=int(input())
l=list(map(int,input().strip().split()))[:n]
s=0
for i in range(len(l)) :
    if l[i]%2!=0 :
        s=s+l[i]
print(s)