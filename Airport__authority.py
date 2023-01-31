t=int(input())
l=[]
for i in range(t):
    n=int(input())
    l.append(n)
w=int(input())
k=0
for i in l :
    if i<=w :
        k+=1
    elif i>w :
        k+=2
print(k)
        
