a=input()
ch=input()
c=0
for i in range(len(a)) :
    if a[i]==ch :
        print('True')
        print(i)
        break
else :
    print("False")