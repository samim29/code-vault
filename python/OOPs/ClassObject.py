class Person:
    name="vishwa"
    age=99
per=Person()

print(per.name) #vishwa
print(per.age) #99

per.hobby="cricket"     #this attributes is only for the 'per' object 
per.lovename="babusona"  #if we creat an another object then it will not have this attributes



#INITIALIZER/CONSTRUCTOR FOR OBJECTS

class Person:
    #initializer/constructor for objects
    def __init__(self,name,age):
        self.name=name
        self.age=age
#creating objects
per1=Person("Tony",43) #we don't need to provide object name

per2=Person("Thor",63)

print(per1.name) #Tony
print(per2.name) #Thor

#OPTIONAL PARAMETER

class Person:
    def __init__(self,name,age=99,hobby="cricket"):
        self.name=name
        self.age=age
        self.hobby=hobby

per1=Person("Vishwa")
per2=Person("Vishwa",21)
per3=Person("Vishwa",43,"Football")

print(per1.hobby) #cricket (default)
print(per3.hobby) #football (changed)

#CLASS AND INSTANCES
class Person:
    country="India" #class attributes ,same for all object
    #initializer/constructor for objects
    def __init__(self,name,age):
        self.name=name
        self.age=age

per1=Person("Tony",43) 

per2=Person("Thor",63)

print(per1.name,per1.country) #class attributes can directly called
print(per2.name,per2.country)
