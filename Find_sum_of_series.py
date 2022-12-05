n=int(input())
s=0
a=1
for i in range(n) :
    s+=(1/(a+i))
print("{:.2f}".format(s))