entry=input("")
a=entry.find("BA")
b=entry.find("AB")
if (a-b==1):
    a=entry.find("BA",a+1)
elif (b-a==1):
    b=entry.find("AB",b+1)
if (a-b>=2 or b-a>=2) and a>=0 and b>=0:
    print("YES")
else:
    print("NO")