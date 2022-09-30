n=int(input())#2
temp=0
if n==0 or n==1 :#n==2 false
    temp=1
for i in range(2,n//2):#i=2
    if n%i==0 :
        temp=1
        break
if temp==0 :
    print("prime")
else :
    print("not a prime")
