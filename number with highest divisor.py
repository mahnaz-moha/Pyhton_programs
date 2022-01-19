def enter(num):
    c=0
    for j in range(1,num+1):
        if (num%j)==0:

            c+=1
    return c

for i in range (1,21):
    numi=int(input(""))
    a=enter(numi)
    numnew=numi
    if i==1:
        cmax=a
        nummax=numnew
    if a>cmax:
        cmax=a
        nummax=numnew
    elif a==cmax:
        if numnew>=nummax:
            nummax=numnew

print(nummax,cmax)



