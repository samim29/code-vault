#METHODS AND ITS TYPE:

#Instance Method

class Person:

    #initializer/constructor for objects
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    #instance/object method
    def findAge(self):
        return self.age

per=Person("tony",63)
print(per.findAge())

#Class Method

class Person:
    country="India"
    #class method 
    @classmethod #decorator
    def greet(cls):
        print("Hello form the ",cls.country)

    #initializer/constructor for objects
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    #instance/object method
    def findAge(self):
        return self.age

per=Person("tony",63)
Person.greet() #calling using class
per.greet() #calling using object

#Static Method

class Person:
    country="India"
    #class method 
    @classmethod #decorator
    def greet(cls):
        print("Hello form the ",cls.country)

    #Static method
    @staticmethod
    def hello():
        print("Hello")

    #initializer/constructor for objects
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    #instance/object method
    def findAge(self):
        return self.age
per=Person("tony",63)      
Person.hello()
per.hello()


