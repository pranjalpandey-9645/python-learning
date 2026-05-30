A = [1, 2, 3, 4]; # List
B = (1, 2, 3, 4); # Tuple
C = {1, 3, 5, 7}; # Set
D = {"name": "john", "age": 30}; # Dictionary
E = "Pranjal"; # String

for i, j in D.items():
    # print(i + " " + j) # this will give error because we cannot concatenate string and integer
    print(i + " " + str(j)) # this will work because we are converting the integer to string before concatenating
    print(i, " " , j) # this will also work because we are using comma to separate the string and integer which will automatically convert the integer to string before printing