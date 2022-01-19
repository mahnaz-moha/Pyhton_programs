class school:
    def __init__(self,name):
        self.name=name

    def get_age(self):
        self.count= int(input(""))
        self.age= input("")
        self.height= input("")
        self.weight= input("")  
        self.age=self.age.split()
        sum_age=0
        for item in self.age:
            sum_age=sum_age+int(item)
            ave_age=(sum_age/self.count)
            
        return ave_age
    def get_height(self):
        self.height=self.height.split()
        sum_height=0
        for item in self.height:
            sum_height=sum_height+int(item)
            ave_height=(sum_height/self.count)
        return ave_height
    def get_weight(self):
        self.weight=self.weight.split()
        sum_weight=0
        for item in self.weight:
            sum_weight=sum_weight+int(item)
            ave_weight=(sum_weight/self.count)
        return ave_weight


    


Information = school("A")
Information1 = school("B")
a=Information.get_age()
b=Information.get_height()
c=Information.get_weight()
a1=Information1.get_age()
b1=Information1.get_height()
c1=Information1.get_weight()
print(a)
print(b)
print(c)
print(a1)
print(b1)
print(c1)
if b>b1:
    print("A")
elif b<b1:
    print("B")
elif b==b1:
    if c>c1:
        print("B")
    elif c<c1:
        print("A")
    else:
        print("Same")