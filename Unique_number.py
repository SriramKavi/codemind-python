n=int(input())
l=list()
temp=0
while n>0 :
    r=n%10
    l.append(r)
    n//=10
for element in l :
    if l.count(element)>1 :
        temp=1
        break
if temp==1:
    print("Not Unique Number")
else :
    print("Unique Number")
