def fun(a) :
    if a%2 :
        a=a**2
    else :
        a=''
    return a

def rev(n) :
    s=0
    while n :
        r=n%10
        s=s*10+r
        n//=10
    return s

a=input()
n=rev(int(a))
k=''
while n :
    r=n%10
    k+=str(fun(r))
    n//=10
print(k)
