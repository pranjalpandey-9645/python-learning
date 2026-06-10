A = [1, 2, 3, 4]; # List
B = (1, 2, 3, 4); # Tuple
C = {1, 3, 5, 7}; # Set
D = {"name": "john", "age": 30}; # Dictionary
E = "Pranjal"; # String

for i, j in D.items():
    # print(i + " " + j) # this will give error because we cannot concatenate string and integer
    '''this will work because we are converting the integer to string before concatenating'''
    print(i + " " + str(j))
    '''this will also work because we are using comma to separate the string and integer
    which will automatically convert the integer to string before printing'''
    print(i, " " , j) 

'''This ("") is the string with leading and trailing spaces.
this ('''''')is a multi line string with leading and trailing spaces.'''

# some of the given Built-in functions
print(len(E))  # prints the length of the string E
print(max(C))  # prints the maximum value in the set C
print(min(C))  # prints the minimum value in the set C
print(pow(12, 3))  # prints the value of 12 raised to the power of 3
print(sum(C))  # prints the sum of all the elements in the set C