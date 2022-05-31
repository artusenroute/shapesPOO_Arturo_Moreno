from rectangle import Rectangle

#Create class Square  that extends Rectangle
class Square(Rectangle):   
        
    def getSide(self):
        return self._width
    
    def setSide(self, side):
        self._width = side
        
    def setWidth(self):
        self._width = width
    
    def setLenght(self):
        self._lenght = lenght


#Get Square Side
if __name__ == '__main__':
    square = Square()
    print(square.getSide())

#Set another side
    square2 = Square()
    square2.setSide(2)
    print(square2.getSide())