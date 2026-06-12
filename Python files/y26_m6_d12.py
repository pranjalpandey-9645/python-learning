class Python:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
     return self.pages + other.pages
    
class Java:
    def __init__(self, pages):
        self.pages = pages
    
obj = Python(320)

obj2 = Java(345)

print(obj + obj2)

