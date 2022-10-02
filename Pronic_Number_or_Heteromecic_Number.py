def pronic(n):
    c=0
    for i in range(n):
        if i*(i+1)==n :
            c+=1
    if n==0:
        print("YES")
    if c==1 :
        print("YES")
    else :
        print("NO")
        
n=int(input())
pronic(n)
