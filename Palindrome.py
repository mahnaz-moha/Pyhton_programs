entry=input("")
a=len(entry)
entry=entry.lower()
b=0
c=0
for i in range(0,a-1):
    if entry[i]==entry[a-i-1]:
        c+=1
    else:
        b+=1
if c==a-1:
    print("palindrome")
else:
    print("not palindrome")



