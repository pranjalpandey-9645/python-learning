'''
# s1 is an object (instance) of the Student class.
# name, age, and marks are instance attributes.
#✨__init__✨ is a special method used to initialize attributes for a new object. 
 Python automatically calls it the moment an object is created. 
 Without __init__, we would have to manually assign attributes to every single 
 object from the outside, or create separate custom methods just to set up each 
 individual attribute, making the code messy and repetitive.

#✨self✨ is a reference to the instance (object) of the class. 
 It is used within class methods to access the object's attributes and other methods.
 The self parameter is not a keyword; it is a convention used in Python to represent 
 the instance of the class. You can name it differently if you prefer,
 but it is highly recommended to stick to the self convention for clarity and consistency.

#✨✨IMPORTANT POINTS WE SHOULD KNOW IN THAT CODE✨✨
1. Student() is the class.
2. __init__(self) is the method to initialize the code, that is 
   used as the automation in the code to call the attributes.
3. talk(self) is also a method that is used inside the code.
4. we can use only one constructor at a time in the class.
'''
class Student:
    def __init__(self):
        self.name = 'Subham'
        self.age = 20
        self.marks = 00
        self.Name = 'Subham'
        
    def talk(self):
        print("Name -", self.name)
        print("Age -", self.age)
        print("Marks -", self.marks)

s1 = Student()
s1.name = 'Daemon' #this will change the name attribute of the instance s1
s1.age = 21 #this will change the age attributes of instance s1
print(s1.name)
print(s1.age) 
print(s1.marks)  # This will print the default marks value of 0

s2 = Student()
s2.name = 'Rohan'
s2.age = 22
s2.marks = 90
print(s2.name)
print(s2.age)
print(s2.marks)  # This will print the marks value of 90 for s2

s1 = Student() # This will overwrite the objects attributes and parameters.
s1.talk() #This is the instance method to call the function. 
print(id(s1))
print(id(s2))