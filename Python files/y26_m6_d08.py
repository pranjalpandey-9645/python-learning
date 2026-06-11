from square import Square as Sq
from triangle import Triangle as Tr

s = Sq()
s.set_width(6)
s.set_height(7)
print(s.area())

t = Tr()
t.set_width(12)
t.set_height(10)
print(t.area())