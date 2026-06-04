# n = input("Name: ")
# a = int(input("Age: "))
# m = int(input("Marks: "))

class Student:
    def __init__(self, n, a, **m):
        self.name = n
        self.age = a
        self.marks = m
        
    def display(self):
        print("Hi ", self.name)
        print("your age ", self.age)
        print("your marks", self.marks)

s1 = Student("Daemon", 18, science = 96, english = 84, maths = 45, java = 12)
s1.display()

print("--------------------")

s2 = Student("Mallhaar", 28, science = 996, english = 884, maths = 445, java = 112)
s2.display()      