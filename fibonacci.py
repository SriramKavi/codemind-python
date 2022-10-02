def fib(n):
    a=0
    b=1
    count=2
    if n<0 :
        print("Enter only +ve values")
    elif n==1 :
        print(a)
    else :
        print(a,end=" ")
        print(b,end=" ")
        while count<n :
            c=a+b
            print(c,end=" ")
            count+=1
            a=b
            b=c
           
n=int(input())
fib(n)
