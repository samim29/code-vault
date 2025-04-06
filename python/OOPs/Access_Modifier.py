#access modifier

class Person:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.__salary=salary #using __ we private it. it can only be accessed in side the class ,not outside the class

    def findAge(self):
        return self.age
    def getSalary(self):
        print(self.__salary)
    
    #private method 
    def __calculateTax(self):
        print("calculating tax")

per=Person("vishwa",99,5000)
print(per.name)

per.getSalary() #it will have the access of salary as salary can acessed inside the class, and the method is defined in side the class
print(per.__salary) #it will not have the acess the salary


#method to acess private attributes or methods:

print(per._Person__salary) #5000