A = [1, 2, 3, 4]; #list
B = (1, 2, 3, 4); #tuple
C = {1, 2, 3, 4}; #set
D = {
    'a': 1, 
     'b': 2, 
     'c': 3, 
     'd': 4
     }; #dictionary

# print(type(A))
# print(type(B))

# for i in range(1, 6, 1):
#     print(i);
# else: 
#     print("the loop is completed");


#STRINGS

"""This is a multi line string
which is used for documentation."""

x = "Hello, World!";
y = 'Hello, World!';

print(x.lower()); #This will convert the string to lowercase
print(y.upper()); #This will convert the string to uppercase
print(x.split(",")); #This will split the string into a list
print(y.replace("World", "Python")); #This will replace a substring with another substring
print(x[0:5]); #This will slice the string from index 0 to 5
print(y[-6:]); #This will slice the string from the 6th character from the end to the end
print(x + " " + y); #This will concatenate two strings
print(x * 2); #This will repeat the string twice