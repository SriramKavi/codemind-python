def sq(a) :
    for i in range(1,a+1) :
        if i*i==a :
            return True
    return False

n=int(input())
l=list(map(int,input().split()))[:n]
s=0
for i in l :
    if sq(i) :
        s+=i
print(s)
