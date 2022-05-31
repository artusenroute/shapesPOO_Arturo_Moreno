from shape import Shape

#Create class Rectangle that extends Shape
class Rectangle(Shape):
    def __init__(self, width = 1.0, lenght = 1.0):
        self._width = width
        self._lenght = lenght
        super().__init__("yellow", True)
        
    def getwidth(self):
        return self._width
    
    def getLenght(self):
        return self._lenght
    
    def setWidth(self, width):
        self._width = width
    
    def setLenght(self, lenght):
        self._lenght = lenght
    
    def getArea(self):
        return int(self._width * self._lenght)
    
    def getPerimeter(self):
        return (int(self._width)*2)+(int(self._lenght)*2)


#Get Rectangle
if __name__ == '__main__':
    retangle = Rectangle()
    print(retangle)

#Get Rectangle Area
    rectangle2 = Rectangle(width= 5, lenght=4)
    print(rectangle2.getArea())

#Get Rectangle Perimeter
    rectangle3 = Rectangle(width= 5, lenght=4)
    print(rectangle3.getPerimeter())