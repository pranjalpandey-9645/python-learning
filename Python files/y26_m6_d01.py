# X[start:end] #items start through end-1
# X[start:end:step] #start through end-1, by step
#X[:end] #items from the beginning through end-1
#X[start:] #items from start through the end of the array,list, or string
#X[::step] #items from the beginning to the end of the array, list, or string, by step
#X[Random:end] #items from the random index to the end of the array, list, or string
#X[:] #a copy of the whole array, list, or string

# -+---+--+---+---+---+-------+---+---+---+---+-------+---+---+---+---+---+---+---+-
#  P   y  t   h   o   n       D   a   i   l   y       P   r   a   c   t   i   c   e
# -+---+--+---+---+---+-------+---+---+---+---+-------+---+---+---+---+---+---+---+-
#  0   1   2   3   4   5       6   7   8   9   10      11  12  13  14  15  16  17  18
# -19 -18 -17 -16 -15 -14     -13 -12 -11 -10  -9      -8  -7  -6  -5  -4  -3  -2  -1

# INDEXING AND SLICING
X = [1, 2, 3, 4, 5, 6, 7, 8, 9];
Y = "JavaScript";
Z = [1, "Aurora", 3.14, True, [1, 2, 3], {"name": "Aurora", "age": 22}];

print(X[0]) #accessing the 1st element of the list X
print(Y[3:]) #accessing the elements from the 4th element to the end of the list Y
print(Z[::2]) #accessing every 2nd element of the list Z
print(X[:]) #accessing all the elements of the list X
print(Y[-2:]) #accessing the last 2 elements of the list Y
print(Z[4][1]) #accessing the 2nd element of the 5th element of the list Z
print(X[::-1]) #accessing the elements of the list X in reverse order
print(Y[3:0:-1]) #accessing the elements of the list Y from the 4th element to the 2nd element in reverse order
print(Z[5]["name"]) #accessing the value of the key "name" in the 6th element of the list Z
print("-------------------------")


#Functions
'''This is the user defined function that takes two parameters and returns the arguments passed to it.
   The def keyword is used to define a function, followed by the function name and parentheses ().'''

def sumf(a, b):
    print(a + b)
sumf(10, 20) #calling the function with arguments 10 and 20
print("-------------------------")


'''Return statement is used to return a value from a function.
 The value can be of any data type, and it can be used in the calling code.'''
def str_greet(name):
    return "Hello " + name + ", welcome to Python programming!"
print(str_greet("Alice")) #calling the function with the argument "Alice"
print("-------------------------")

def dataty(inp1, inp2):
    if type(inp1) == type(inp2):
        return inp1 + inp2
    elif type(inp1)==str and type(inp2) == int:
        return inp1 * inp2
    else:
        return "Input data types are not the same"
print(dataty(10, 20)) #calling the function with arguments 10 and 20
print(dataty("Predator-x\n", 2)) #calling the function 2 times in a string in a column
print(dataty(10, "Predator-x\n")) #calling the function with arguments of different data types
print("-------------------------")