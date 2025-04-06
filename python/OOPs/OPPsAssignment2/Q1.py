'''1.Implement an abstract class Shape with an abstract method calculate_area(). Create subclasses such as Rectangle and Circle that inherit from Shape and override
the calculate_area() method to calculate the area of their respective shapes.
'''

from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        return self.length*self.width

class Circle(Shape):
    pi=3.14
    def __init__(self, radius) :
        self.radius=radius
    def calculate_area(self):
        return Circle.pi*(self.radius)**2
# Example usage
def main():
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(15.0, 7.0)
    circle = Circle(2.5)

    # Calculate and print the areas
    print("Rectangle area:", rectangle.calculate_area())
    print("Circle area:", circle.calculate_area())

if __name__ == "__main__":
    main()
        

        