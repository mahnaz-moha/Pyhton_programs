entry=int(input(""))
counter=dict()
lst=[]
for i in range(0,entry):
    name_country=input("")
    lst.append(name_country)
    
for letter in lst:
    counter[letter]=counter.get(letter,0)+1
a=list(counter.keys())
a.sort()
for this_one in a:
    print(this_one,counter[this_one])