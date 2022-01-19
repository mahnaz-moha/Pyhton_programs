from datetime import date
def calculateAge(birthDate):
    today=date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

d=input()
year=d[0:4]
month=d[5:7]
day=d[8:]
if int(month)<=0 or int(month)>12:
    print("WRONG")
elif int(day)<=0 or int(day)>31:
    print("WRONG")
elif int(month)==2 and int(day)>29:
    print("WRONG")
elif int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) ==11 and int(day) > 30:
    print("WRONG")
else:
    print(calculateAge(date(int(year),int(month),int(day))))
