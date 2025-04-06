
#composition
class Engine:
    def engineDetails(self):
        print("Car engine is model E1213")

class Tyres:
    def tyreDetails(self):
        print("Car tyre is apollo")

class Doors:
    def doorDetails(self):
        print("Doors of the car is automatic")

class Car:
    def __init__(self) :
        self.engine=Engine()
        self.tyres=Tyres()
        self.doors=Doors()
    
    def printDetails(self):
        self.engine.engineDetails()
        self.tyres.tyreDetails()
        self.doors.doorDetails()

c=Car()
c.printDetails()