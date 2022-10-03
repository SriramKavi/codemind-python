def fib(n) :
    k=n
    a=0
    b=1
    count=2
    l=list()
    if n<0 :
        print("Enter only positive values")
    elif n==0 or n==1 :
        print("True")
    else :
        while count<=n :
            c=a+b
            l.append(c)
            a=b
            b=c
            count+=1
        if n==2 or n==3 :
            print("True")
        elif k in l :
            print("True")
        else :
            print("False")
            


n=int(input())
k=n
fib(n)
    
