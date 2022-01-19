

def Convert(string): 
    li = list(string.split("+")) 
    return li 
      
str1 = input("")
b=Convert(str1) 

b.sort()


def listToString(b):  
    
    str1 = "+" 
    return (str1.join(b)) 
        
        
print(listToString(b)) 
