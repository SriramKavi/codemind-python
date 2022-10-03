def rev(n) :
    global s
    s=0
    while n :
        r=n%10
        s=s*10+r
        n//=10
    return s
def is_prime(n) :
    t=0
    if n==0 or n==1 :
        print("not a prime")
    else :
        for i in range(2,n) :
            if n%i==0 :
                t=1
                break
        return t
def pr(s) :
    k=rev(n)
    global temp
    temp=0
    for j in range(2,k) :
        if k%j==0 :
            temp=1
            break
    return temp
def circularprime(n) :
    a=is_prime(n)
    b=pr(s)
    if a==0 and b==0 :
        print("circular prime")
    else :
        for m in range(2,n) :
            if n%m==0 :
                print("not prime")
                break
        else :
            print("prime but not a circular prime")


n=int(input())
k=rev(n)
pr(s)
circularprime(n)
is_prime(n)
