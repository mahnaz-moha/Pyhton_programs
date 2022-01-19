class Human:
    def __init__(self,name):
        self.name=name

class Footbalist(Human):
    
    def value(self):
        import random
        n=["A","B"]
        answer= random.choice(n)
        return (self.name,answer)


footbalist1=Footbalist(" حسین")
footbalist2=Footbalist("مازیار")
footbalist3=Footbalist("اکبر")
footbalist4=Footbalist("نیما")
footbalist5=Footbalist("مهدی")
footbalist6=Footbalist("فرهاد")
footbalist7=Footbalist("محمد")
footbalist8=Footbalist("خشایار")
footbalist9=Footbalist("میلاد")
footbalist10=Footbalist("مصطفی")
footbalist11=Footbalist("امین")
footbalist12=Footbalist("سعید")
footbalist13=Footbalist("پویا")
footbalist14=Footbalist("پوریا")
footbalist15=Footbalist("رضا")
footbalist16=Footbalist("علی")
footbalist17=Footbalist("بهزاد")
footbalist18=Footbalist("سهیل")
footbalist19=Footbalist("بهروز")
footbalist20=Footbalist("شهروز")
footbalist21=Footbalist("سامان")
footbalist22=Footbalist("محسن")
print(footbalist1.value())
print(footbalist2.value())
print(footbalist3.value())
print(footbalist4.value())
print(footbalist5.value())
print(footbalist6.value())
print(footbalist7.value())
print(footbalist8.value())
print(footbalist9.value())
print(footbalist10.value())
print(footbalist11.value())
print(footbalist12.value())
print(footbalist13.value())
print(footbalist14.value())
print(footbalist15.value())
print(footbalist16.value())
print(footbalist17.value())
print(footbalist18.value())
print(footbalist19.value())
print(footbalist20.value())
print(footbalist21.value())
print(footbalist22.value())