#Encapsulation

class Person:
    #initializer/constructor for objects
    def __init__(self,name,car):
        self.__name=name
        self.__car=car



    # Getter and Setter method- Public method to allow the contolled interactions
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name
    def getCar(self):
        return self.__car
    def setCar(self,car):
        self.__car= car


per=Person("Tony","BMW") 
print(per.getName())
per.setName("Sk Samim ALi")
print(per.getName())