n=int(input())
l=list(map(int,input().split()))[:n]
fh=[]
sh=[]
for i in l[0:n//2] :
    sh.append(i)
for j in l[-1:-((n//2)+1):-1] :
    fh.append(j)
fh.extend(sh)
print(*fh)
