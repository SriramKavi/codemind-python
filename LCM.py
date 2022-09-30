def LCM(a,b) :
    if a>b :
        maxi=a
    else :
        maxi=b
    v=maxi
    while True :
        if maxi%a==0 and maxi%b==0 :
            print(maxi)
            break
        else :
            maxi=maxi+v

a,b=map(int,input().split())
LCM(a,b)
