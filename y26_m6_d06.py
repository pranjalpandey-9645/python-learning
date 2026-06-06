class Polygon():
    __width = None
    __height = None
    
    def set_width(self, width):
        self.__width = width
    
    def get_width(self):
       return self.__width

    def set_height(self, height):
        self.__height = height
    
    def get_height(self):
       return self.__height
    
class Square(Polygon):
    def area(self):
        print(self.get_height() * self.get_width())
    
class Triangle(Polygon):
    def area(self):
        print(self.get_height() * self.get_width() * 1/2)

s = Square()
s.set_height(12)
s.set_width(10)
s.area()

t = Triangle()
t.set_height(11)
t.set_width(11)
t.area()