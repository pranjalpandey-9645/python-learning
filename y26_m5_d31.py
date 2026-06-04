class Student:
    def __init__(self):
        self.name = 'Subham'
        self.age = 20
        self.marks = 00
        
    def talk(self):
        print("Name -", self.name)
        print("Age -", self.age)
        print("Marks -", self.marks)

s1 = Student()
s1.name = 'Daemon' #this will change the name attribute of the instance s1
s1.age = 21
print(s1.name)  # This will print the default marks value of 0
print(s1.age) 
print(s1.marks)  # This will print the default marks value of 0

s2 = Student()
s2.name = 'Rohan'
s2.age = 22
s2.marks = 90
print(s2.name)
print(s2.age)
print(s2.marks)  # This will print the marks value of 90 for s2