lst=[]
lst1=[]
a=0
number_lap=int(input(""))

for i in range(0,number_lap):
    price_quality=input("")
    price_quality=price_quality.split()
    lst.append(price_quality[0])
    lst1.append(price_quality[1])

def find_better(number_lap):
    for i in range(number_lap):
        for j in range(number_lap):
            if (int(lst[i])>int(lst[j]) and (i!=j)):
                if int(lst1[i])<int(lst1[j]) :
                    return("happy irsa") 
             
    return("poor irsa")
print(find_better(number_lap))
    