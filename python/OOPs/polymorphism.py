
#Polymorphism 
#polymorphism using inheritance

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def eat(self):
        print("Dog is eating") #method overriding

class Cat(Animal):
    def eat(self):
        print("Cat is eating")  ##method overriding

c=Cat()
d=Dog()
a=Animal()

c.eat()
d.eat()
a.eat()



#Duck typing concept

class BirdFly:
    def flyBird(self,bird):
        bird.fly()

class Parrot:
    def fly(self):
        print("Parrot is flying")

class crow:
    def fly(self):
        print("Crow is flying")

p=Parrot()
c=crow()
bf=BirdFly()

bf.flyBird(p)
bf.flyBird(c)

