a=input()
a=a.lower()
k=[a[i] for i in range(len(a)-1,-1,-1)]
v=''.join(k)
if a==v :
    print("True")
else :
    print("False")
