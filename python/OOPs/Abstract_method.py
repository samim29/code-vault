#abstract class
from abc import ABC, abstractmethod
class Animal(ABC) :
    @abstractmethod
    def eat(self):
        pass


class Dog(Animal):
    def sleep(self):
        print("Dog is sleeping")
    
    def eat(self):
        print("Dog is eating")

d=Dog()