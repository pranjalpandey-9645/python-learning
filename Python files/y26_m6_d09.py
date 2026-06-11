class Parent:
    def __init__(self, name):
        print("Parent__init__ method", name)

class Parent2:
    def __init__(self):
         print("Parent2__init__method")

class Child(Parent, Parent2):
    def __init__(self):
        print("Child__init__")
        Parent.__init__(self, "Subham")
        Parent2.__init__(self)
        # super().__init__("Subham")

child_obj = Child()
print(Child.__mro__)
