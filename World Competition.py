n_players=input("")
times=input("")
times=times.split()
c=0
for item in times:
    if int(item)<=2:
        c+=1
c=int(c/3)
print(c)
    