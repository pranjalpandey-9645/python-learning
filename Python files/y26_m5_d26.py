std = input("student name:");
std = str(std);
print("the name of the student is ", std);

if std == "a":
    print("the student is belongs to class 10th");
elif std == "b":
    print("the student is belongs to class 11th");
elif std == "c":
    print("the student is belongs to class 12th");
else:
    print("invalid student name");

x = 20;

while x <= 30:
    print("the value of x is ", x);
    x = x + 1;

# For loop

A = [1, "P", 2, "Q"]; # List
B = (1, 2, 3, 4); # Tuple
C = {1, 3, 5, 7}; # Set
D = {"name": "john", "age": 30}; # Dictionary
E = "Pranjal"; # String

for i in A:
    print("the Element of A", i);
    print(type(i));
for i in B:
    print("the Element of B", i);
    print("the Type of B", type(i));
for i in C:
    print("the Element of C", i);
    print("the Type of C", type(i));
for i in D:
    print("the Element of D", i);
    print("the Type of D", type(i));
for i in E:
    print("the Element of E", i);
    print("the Type of E", type(i));
for i in D.values():
    print(i);