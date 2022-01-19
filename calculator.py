class Calculator:

   def add(self, x, y):
       self.x = x
       self.y = y
       a = self.x + self.y
       return a
    
   def subtract(self, x, y):
       self.x = x
       self.y = y
       a = self.x - self.y
       return a
    

   def multiply(self, x, y):
       self.x = x
       self.y = y
       a = self.x * self.y
       return a
    

   def divide(self, x, y):      
       self.x = x
       self.y = y
        
       if (y == 0):
           a = "You can't divide by zero!"
       else:
           a = self.x / self.y  
    
       return a

num=Calculator()
print(num.subtract(12,15))
print(num.divide(12,15))
print(num.multiply(12,15))
print(num.add(12,15))