c=cmax=nummax=c_prime=0
for i in range(1, 11):
    entryi=int(input(""))
    c=0
    for j in range (2, entryi):
        if entryi%j==0:
            #print("bakhshpazir:",j)
            c_prime=0
            for y in range (1, j):#check avval budan
                if j%y==0:
                    c_prime+=1
            #print("c_prime:", c_prime)
            if c_prime<=1:
                #print("avval:",j)
                c+=1
    if c>cmax:
        cmax=c
        nummax=entryi
        #print("cmax:", cmax)
    elif c==cmax:
        if entryi>nummax:
            nummax=entryi
print(nummax,cmax)

    