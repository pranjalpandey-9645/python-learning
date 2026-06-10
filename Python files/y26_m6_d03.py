# n = input(str("Name : "))
# a = int(input("Age : "))
# m = int(input("Marks : "))

class Student():
    def __init__(self, n, a, **m):
        self.name = n
        self.age = a
        self.marks = m

    def display(self):
        print("Hey there ", self.name)
        print("your age is", self.age)
        print("And your marks are ", self.marks)

s1 = Student("Pranjal", 80, English=90, Mathematics=70, Science=85)
s1.display()

'''
# There are som changes we can apply there in the code for example: 
1. I can put the default vlaue of m wright in the code "def __init__(self, n, a, m=54)"
   this will print the default value of marks m.
2. I can change the code in a way like 
   def __init__(self, n, a, **m):
   s1 = Student("lufy", 20, English=60, Mathematics=80, Science=70)
   instead of using n = input("Name - ")
'''