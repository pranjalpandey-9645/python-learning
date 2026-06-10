'''💻Types of arguments in a function:✨'''
'''
🧿 1.Positional arguments: These are the most common type of arguments, 
where the values are passed in the same order as the parameters defined in the function.'''
'''
🧿 2.Keyword arguments: These are the arguments where the values are passed using the 
parameter names, regardless of the order.'''
'''
🧿 3.Default arguments: These are the arguments that have a default value assigned to them. 
If the caller does not provide a value for that argument, the default value will be used.'''
'''
🧿 4.Variable-length arguments: These are the arguments that can take an arbitrary number of values. 
There are two types of variable-length arguments:   
a. ✨*args: This allows the function to accept any number of positional arguments. 
The arguments are passed as a tuple.
b. ✨**kwargs: This allows the function to accept any number of keyword arguments.
'''

# EXAMPLES
# 1. Positional arguments
def sum (a, b):
    print(a + b)
sum(5, 10) #calling the function with positional arguments
print("-------------------------")
def addd(name, age):
    print("Name -", name)
    print("Age -", age)
# addd("Shrikant", 20) #calling the function with positional arguments
print("-------------------------")
def addd(inp1, inp2):
   
   if type(inp1) == str and type(inp2) == int:
     return inp1 + " is " + str(inp2) + " years old."
   elif type(inp1) == type(inp2):
        return inp1 + inp2

print(addd(20, 22)) #calling the function with positional arguments of same data type
print(addd("Vardhan", 20)) #calling the function with positional arguments

# # Keyword arguments
def greet(name, Model, Company):
    print("Name -", name)
    print("Model -", Model)
    print("Company -", Company)

greet(name="John", Model="Camry", Company="Toyota") # calling the function with keyword arguments

# Default arguments
def greet(name, Model="Camry", Company="Toyota"):
    print("Name -", name)
    print("Model -", Model)
    print("Company -", Company)

greet(name="John") # calling the function with default arguments
greet(name="Alice", Model="Civic") # calling the function with default arguments and keyword arguments
greet(name="Bob", Company="Honda") # calling the function with default arguments and keyword arguments

# '''🧿**marks is a variable-length keyword argument that can take any number of keyword arguments
# and it is passed as a dictionary to the function. The items() method is used to iterate through 
# the dictionary and print the key-value pairs.⬇️'''

def class_of_std(name, age, **marks):
    print("Name -", name)
    print("Age -", age)
    # print("Marks -")
    for x, y in marks.items():
        print(x, "-", y)

class_of_std(name="Subham", age=20, English=90, Mathematics=85, Science=95) # calling the function with keyword arguments

# Local and global variables
x = 10 # global variable
y = 20 # global variable

def sum(x, y):
    global  z # declaring z as a global variable
    z = 30 # local variable
    print(z) # This will print the value of local variable z
    print(x) # This will print the value of Global variable x, which is 10.
    print(y) # This will print the value of Global variable y, which is 20.

sum(x, y) # calling the function to print the sum of local variables
print("-------------------------")
print(x)
print(y)
print(z) # This will raise an error because z is a local variable and cannot be accessed outside the function.

'''to make the z gloabally accessible we can use the global keyword inside the function
 to declare z as a global variable.⬇️'''