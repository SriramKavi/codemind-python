a=input()
k=a.lower()
v='aeiou'
c=0
k=[]
l=[]
for i in a :
    if i in v :
        k.append(i)
for j in k :
    if j not in l :
        l.append(j)
for x in l :
    c+=1
if c==5 :
    print('True')
else :
    print('False')
