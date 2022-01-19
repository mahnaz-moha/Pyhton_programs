number_numbers=int(input(""))
from math import sqrt
import decimal
lst=[]    
for i in range(0,number_numbers):
    numbers=int(input(""))
    a=sqrt(numbers)
    
    lst.append(a)   

for item in lst:
    b=int((item)*10000)/10000
    #print(b,type(b))
    print("%.4f"%b)
    #print(b)
    #print(c)
    #c=float(c)
    

    
    