class Rectangle():
    def __init__(self,length,breath):
        self.length=length
        self.breadth=breath


    def getArea(self):
        print(self.length*self.breadth, "Area of rectangle")



class Sqaure(Rectangle):
    def __init__(self,side):
        self.side= side
        Rectangle.__init__(self,side, side)
    def getArea(self):
        print(self.side* self.side,"Area of sqaure")
square=Sqaure(4)
square.getArea()

reactangle=Rectangle(4,5)
reactangle.getArea()
