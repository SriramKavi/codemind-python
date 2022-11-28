def rev(k) :
    for i in range(len(k)-1,-1,-1) :
        l.append(k[i])
    return l

a=input()
k=a.split()
l=[]
x=rev(k)
sen=' '.join(x)
print(sen)