def vowel_count(a) :
    count=0
    v='aeiouAEIOU'
    for i in a :
        if i in v :
            count+=1
    return count

a=input()
k=a.split()
c=0
dic={ }
for i in k :
    vc=vowel_count(i)
    dic[i]=vc
for n,m in dic.items() :
    if m==min(dic.values()) :
        c+=1
print(c)
