 #Implicit method overloading

class Calculator:
    def add(self,a,b,c=0):
        return a+b+c
    
cal=Calculator()
print(cal.add(2,3,4))
print(cal.add(2,3))