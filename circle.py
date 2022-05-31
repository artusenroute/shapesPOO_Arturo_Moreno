from shape import Shape
import numpy as np
#Create class Circle that extends Shape
class Circle(Shape):
    def __init__(self, radius = 1.0):
        self._radius = radius
        super().__init__("black", False)
    
    def getRadius(self):
        return self._radius
    
    def setRadius(self, radius):
        self._radius = radius
    
    def getArea(self):
        return np.pi * int(self._radius)**2
    
    def getPerimeter(self):
        return np.pi * int(self._radius)*2 

#Get Circle
if __name__ == '__main__':
    circle = Circle()
    print(circle)

#Get Circle Area
    circle2 = Circle(radius = 4)
    print(circle2.getArea())

#Ger Circle Perimeter
    circle3 = Circle(radius = 4)
    print(circle3.getPerimeter())