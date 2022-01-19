entry=input()
entry=entry.split()
entry=[int(entry[0]),int(entry[1]),int(entry[2])]
entry.sort()
a=entry[1]-entry[0]
b=entry[2]-entry[1]
c=a+b
print(c)
