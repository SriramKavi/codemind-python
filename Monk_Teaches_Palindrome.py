def pal(v) :
    
    k=''
    for i in range(len(v)-1,-1,-1) :
        k+=v[i]
    return k
        
        

t=int(input())
for x in range(t) :
    a=input()
    if pal(a)==a :
        if len(pal(a))%2==0 :
            print("YES EVEN")
        else :
            print("YES ODD")
    else :
        print("NO")
        