n=int(input())
no_of_digits=len(str(n))
t=pow(n,2)
ld=t%pow(10,no_of_digits)
if ld==n :
    print("Automorphic Number")
else :
    print("Not an Automorphic Number")
