n=int(input())#5
l=list(map(int,input().strip().split()))[:n]#1 2 3 4 5
sum=0
for i in range(len(l)):#(0,5)
    if l[i%2]==l[0] :
        sum=sum+l[i]
print(sum)
        

