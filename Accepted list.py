num=int(input(""))
entryi_s=[]
for i in range (1,num+1):
    entryi=input("")
    entry_joda=entryi.split(".")
    name=entry_joda[1]
    name=name.title()
    entry_joini=entry_joda[0]+" "+name+" "+entry_joda[2]
    entryi_s.append(entry_joini)
entryi_s.sort()
#print(entryi_s)
for letter in entryi_s:
    print(letter)
