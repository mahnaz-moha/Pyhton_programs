lst=[]
for i in range(0,3):
    numi=int(input(""))
    if numi in lst:
        print("same number")
        break
    else:
        lst.append(numi)
        
if len(lst)==3: 
    lst.sort()
    print(lst[1])



