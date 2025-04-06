#inheritance

class Animal:
    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print(self.name + " animal is eating")

class Dog(Animal):
    def __init__ (self,name,type):
        #call the constructor/initializer of the Animal class
        Animal.__init__(self,name)
        self.type=type
    
dog=Dog("Moti","German Shephered")

dog.eat()


#Access parent property using supar keyword

class Parent:
    property = 90

    def eat(self):
        print("Parent is eating")

class Child(Parent):
    property=99
    
    #calling parent property using super

    def display(self):
        print("Child property ",self.property)
        print("Parent property ",super().property)

    #calling parent method using super

    def eat(self): #method overiding (same name method in parent and child)
        print("Child is eating")
    
    def callEat(self):
        self.eat() #calling eat method of the child
        super().eat()#calling eat method of Parent


obj=Child()
obj.display()
obj.callEat()



#using super for calling parent constructor or initializer

class Animal:
    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print(self.name + " animal is eating")

class Dog(Animal):
    def __init__ (self,name,type):
        #call the constructor/initializer of the Animal class
        # Animal.__init__(self,name) #we will use super instead of Animal 
        super().__init__(name) #we don't need to provide self
        self.type=type

dog=Dog("Moti","German Shephered")

dog.eat()


#TYPE OF UNHERITANCE

#SINGLE INHERITANCE


class Animal:
    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print(self.name + " animal is eating")

class Dog(Animal):
    def __init__ (self,name,type):
    
        super().__init__(name) #single inheritance
        self.type=type


#multilable inheritance (Pet is child of Dog which is child of Anmal)

class Animal:
    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print(self.name + " animal is eating")

class Dog(Animal):
    def __init__ (self,name,type):
    
        super().__init__(name) #single inheritance
        self.type=type

class pet(Dog):
    def __init__(self,name,type,houseName):
        super().__init__()(name,type)
        self.houseName=houseName #multiplevel inheritance


#heirarchial inheritance ( Dog and Cat both are child of Animal)

class Animal:
    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print(self.name + " animal is eating")

class Dog(Animal):
    def __init__ (self,name,type):
    
        super().__init__(name) #heirarchial inheritance
        self.type=type

class Cat(Animal):
    def __init__(self, name,type):
        super().__init__(name)
        self.type=type #heirchial in heritance


#MULTIPLE INHERITANCE (C has two parents A and B)

class A:
    def meth1(self):
        print("Hello from A")

class B:
    def meth2(self):
        print("Hello from B")

class C(A,B):
    def meth(self):
        print("Hello from the child")
    
c=C()#creating object of C

c.meth1()
c.meth2()

#MRO


class A:
    def meth(self):
        print("Hello from A")

class B:
    def meth(self):
        print("Hello from B")

class C(A,B):
    def meth1(self):
        print("Hello from the child")
    
c=C()#creating object of C

c.meth() #Hello from A  (As A comes first in (A,B))  (if it was written a s(B,A) , then output will be Hello fom B as B comes first) 


#Hybrid Inheritance

class Pet(Dog,Cat):
    pass





    