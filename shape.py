from abc import ABC, abstractmethod
#Create the class Shape
class Shape(ABC):
    def __init__(self,color = 'red', filled = True):
        self._color = color
        self._filled = filled
    
    def getColor(self):
        return self._color
    
    def setColor(self, color):
        self._color = color
        
    def isFilled(self):
        return self.filled
    
    def setFilled(self, filled):
        self._filled = filled

    @abstractmethod
    def getArea(self):
        pass
    
    @abstractmethod
    def getPerimeter(self):
        pass
        
    def __str__(self):
        try:
            shape = 'Color? :'+self._color +', '+'Is filled? :'+str(self._filled)+ ", This Radios: "+str(self._radius)
        except:
            try:
                shape = 'Color? :'+self._color +', '+'Is filled? :'+str(self._filled)+ ", This widht: "+str(self._width)+ ", This lenght: "+str(self._lenght)
            except:
                shape = 'Color? :'+self._color +', '+'Is filled? :'+str(self._filled)
        return shape    


#Get Shape
if __name__ == '__main__':
    shape = Shape()
    print(shape)