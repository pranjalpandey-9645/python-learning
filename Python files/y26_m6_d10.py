'''
#Composition is used when we cannot directly
 inherit the whole class.
'''
# Example:

class Circle:
    def __init__(self, radius, circumference):
        self.radius = radius
        self.circumference = circumference

    def radius_c(self, marvel):
      return self.radius*12 / self.circumference 
    

class Polygon:
    def __init__(self, radius, circumference):
        self.area = Circle(radius, circumference)

    def area_m(self, h):
        return self.area.radius_c()

pc = Polygon()
# pc.area(30)
print(pc.area_m())