"""4.Write a Python program that models different animals and their sounds. Design a base class called `Animal` with a method `make_sound()`. Create subclasses like `Dog` and `Cat` that override the `make_sound()` method to produce appropriate sounds.

Tasks:
1. Define the `Animal` class with a method `make_sound()`.
2. Create subclasses `Dog` and `Cat` that override the `make_sound()` method.
3. Implement the sound generation logic for each subclass.
4. Test the program by creating instances of `Dog` and `Cat` and calling the `make_sound()` method.


"""

class Animal:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print("Animal make sound")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        print("The dog barks")

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        print("The cat meow")

animal=Animal("Ani")
dog1=Dog("Bool Dog")
cat1=Cat("Mini")
animal.make_sound()
dog1.make_sound()
cat1.make_sound()
print(f"{animal.name}")
print(f"{dog1.name}")
print(f"{cat1.name}")

