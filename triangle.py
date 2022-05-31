from shape import Shape
import numpy as np

#Create class Equilateral Triangle that extends Shape
class EqTrian(Shape):
    def __init__(self, sideLenght = 1.0):
        self._sideLenght = sideLenght
        super().__init__("black", False)
    
    def getSideLenght(self):
        return self._sideLenght
    
    def setSideLenght(self, radius):
        self._sideLenght = sideLenght
    
    def getArea(self):
        hsquare = (self._sideLenght**2) - ((self._sideLenght/2)**2)
        h = np.sqrt(hsquare)
        return h * self._sideLenght / 2
    
    def getPerimeter(self):
        return self._sideLenght * 3 


#Get triangle side length
if __name__ == '__main__':
    triangle = EqTrian()
    print(triangle.getSideLenght())

    #Get Triangle Area with side length = 3

    triangle2= EqTrian(sideLenght= 3)
    print(triangle2.getArea())

#Get Triangle Perimeter
if __name__ == '__main__':
    triangle3 = EqTrian(sideLenght= 9)
    print(triangle3.getPerimeter())